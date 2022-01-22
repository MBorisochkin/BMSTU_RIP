package com.example.pizzaapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.view.get
import com.example.pizzaapp.databinding.ActivityUpdateBinding
import com.example.pizzaapp.network.Pizza
import com.example.pizzaapp.network.RetrofitInstance
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class UpdateActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUpdateBinding

    override fun onCreate(savedInstanceState: Bundle?) { // Переопределение метода onCreate
        super.onCreate(savedInstanceState)
        binding = ActivityUpdateBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Получение данных из detail activity
        val bundle: Bundle? = intent.extras
        val pizzaName = bundle!!.getString("name")
        val pizzaTopping = bundle.getString("topping")
        val pizzaDiameter = bundle.getInt("diameter")
        val pizzaPK = bundle.getInt("pk")

        // Установка полученных значений во View
        binding.etPizzaName.setText(pizzaName)
        binding.etPizzaTopping.setText(pizzaTopping)

        when(pizzaDiameter){
            23 -> binding.rbD23.toggle()
            30 -> binding.rbD30.toggle()
            35 -> binding.rbD35.toggle()
            40 -> binding.rbD40.toggle()
        }

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

            val pizza = Pizza(pizzaPK, name, topping, diameter)
            RetrofitInstance.api.updatePizza(pizza.pk!!, pizza).enqueue(object : Callback<Pizza> {
                override fun onResponse(
                    call: Call<Pizza>,
                    response: Response<Pizza>
                ) {
                    Toast.makeText(applicationContext, "Успех", Toast.LENGTH_SHORT).show()
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