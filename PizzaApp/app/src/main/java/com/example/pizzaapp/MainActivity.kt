package com.example.pizzaapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.core.view.isVisible
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.pizzaapp.databinding.ActivityMainBinding
import com.example.pizzaapp.network.Pizza
import com.example.pizzaapp.network.PizzaAdapter
import com.example.pizzaapp.network.RetrofitInstance
import retrofit2.HttpException
import retrofit2.Response
import java.io.IOException

const val TAG = "MainActivity"


class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private lateinit var pizzaAdapter: PizzaAdapter

    lateinit var response : Response<List<Pizza>>

    override fun onCreate(savedInstanceState: Bundle?) { // Переопределение метода onCreate
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }

    override fun onStart() { // Переопределение метода onStart
        super.onStart()
        setupRecyclerView() // Установка RecyclerView

        // Корутин для загрузки данных из API
        lifecycleScope.launchWhenStarted {
            binding.progressBar.isVisible = true
            response = try {
                RetrofitInstance.api.getPizzas()
            } catch (e: IOException) { // Обработка ошибки ввода-вывода
                Log.e(TAG, "IOException, you might not to have internet connection")
                binding.progressBar.isVisible = false
                return@launchWhenStarted
            } catch (e: HttpException) { // Обработка ошибки HTTP
                Log.e(TAG, "HttpException, unexpected response")
                binding.progressBar.isVisible = false
                return@launchWhenStarted
            }

            // Проверка успешного ответа
            if(response.isSuccessful && response.body() != null) {
                pizzaAdapter.pizzas = response.body()!!
            } else {
                Log.e(TAG, "Response not successful")
            }
            binding.progressBar.isVisible = false
        }

        // Обработка события нажатия кнопки для добавления записи
        binding.btnCreatePizza.setOnClickListener {
            val intent = Intent(this@MainActivity, CreatePizzaActivity::class.java)
            startActivity(intent)
        }
    }

    // Функция для установки RecyclerView
    private fun  setupRecyclerView() = binding.rvPizzas.apply {
        pizzaAdapter = PizzaAdapter()
        adapter = pizzaAdapter
        layoutManager = LinearLayoutManager(this@MainActivity)

        pizzaAdapter.setOnItemClickListener(object :PizzaAdapter.onItemClickListener {
            override fun onItemClick(position: Int) { // Обработка нажатия на ViewHolder

                val intent = Intent(this@MainActivity, DetailActivity::class.java)
                intent.putExtra("pk", response.body()!![position].pk)
                intent.putExtra("name", response.body()!![position].name)
                intent.putExtra("topping", response.body()!![position].topping)
                intent.putExtra("diameter", response.body()!![position].diameter)
                startActivity(intent)

            }
        })
    }
}