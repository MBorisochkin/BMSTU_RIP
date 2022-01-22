package com.example.pizzaapp

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.pizzaapp.databinding.ActivityDetailBinding
import com.example.pizzaapp.network.Pizza
import com.example.pizzaapp.network.RetrofitInstance
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class DetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDetailBinding

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) { // Переопределение метода onCreate
        super.onCreate(savedInstanceState)
        binding = ActivityDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Получение данных из главной activity
        val bundle: Bundle? = intent.extras
        val pizzaName = bundle!!.getString("name")
        val pizzaTopping = bundle.getString("topping")
        val pizzaDiameter = bundle.getInt("diameter")
        val pizzaPK = bundle.getInt("pk")

        binding.tvPizzaName.text = pizzaName
        binding.tvPizzaTopping.text = "Состав: $pizzaTopping"
        binding.tvPizzaDiameter.text = "Диаметр: $pizzaDiameter см"

        // Обработка события нажатия кнопки для изменения записи
        binding.btnChange.setOnClickListener {
            val intent = Intent(this, UpdateActivity::class.java)
            intent.putExtra("pk", pizzaPK)
            intent.putExtra("name", pizzaName)
            intent.putExtra("topping", pizzaTopping)
            intent.putExtra("diameter", pizzaDiameter)

            startActivity(intent)
        }

        // Обработка события нажатия кнопки для удаления записи
        binding.btnDelete.setOnClickListener {
            RetrofitInstance.api.deletePizza(pizzaPK).enqueue(object : Callback<Pizza> {
                override fun onResponse(call: Call<Pizza>, response: Response<Pizza>) {
                    Toast.makeText(applicationContext, "Удалено", Toast.LENGTH_SHORT).show()
                }

                override fun onFailure(call: Call<Pizza>, t: Throwable) {
                    Toast.makeText(applicationContext, "Ошибка", Toast.LENGTH_SHORT).show()
                }
            })

            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }
}