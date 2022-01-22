package com.example.pizzaapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.view.get
import com.example.pizzaapp.databinding.ActivityCreatePizzaBinding
import com.example.pizzaapp.network.Pizza
import com.example.pizzaapp.network.RetrofitInstance
import retrofit2.Call
import retrofit2.Response


class CreatePizzaActivity : AppCompatActivity() {

    private lateinit var binding : ActivityCreatePizzaBinding

    override fun onCreate(savedInstanceState: Bundle?) { // Переопределение метода onCreate
        super.onCreate(savedInstanceState)
        binding = ActivityCreatePizzaBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Обработка события нажатия кнопки для сохранения изменений
        binding.btnSave.setOnClickListener {

            val name = binding.etPizzaName.text.toString()
            val topping = binding.etPizzaTopping.text.toString()

            val diameter = when(binding.rgDiameter.checkedRadioButtonId) {
                binding.rgDiameter[0].id-> 23
                binding.rgDiameter[1].id -> 30
                binding.rgDiameter[2].id -> 35
                binding.rgDiameter[3].id -> 40
                else -> 23
            }

            // Проверка пустых полей
            if (name.isNotEmpty() && topping.isNotEmpty())
            {
                RetrofitInstance.api.createPizza(name, topping, diameter)
                    .enqueue(object : retrofit2.Callback<Pizza> {
                        override fun onResponse(call: Call<Pizza>, response: Response<Pizza>) {
                            Toast.makeText(applicationContext, "Успех", Toast.LENGTH_LONG).show()
                        }

                        override fun onFailure(call: Call<Pizza>, t: Throwable) {
                            Toast.makeText(applicationContext, "Ошибка", Toast.LENGTH_SHORT).show()
                        }
                    })

                val intent = Intent(this, MainActivity::class.java)
                startActivity(intent)
            }
            else
                Toast.makeText(applicationContext, "Неверные данные", Toast.LENGTH_SHORT).show()
        }
    }
}