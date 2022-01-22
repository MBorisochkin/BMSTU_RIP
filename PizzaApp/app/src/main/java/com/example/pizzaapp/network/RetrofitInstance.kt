package com.example.pizzaapp.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance { // Экземпляр объекта Retrofit

    val api: PizzaApi by lazy {

        Retrofit.Builder() // Построение объекта класса Retrofit
            .baseUrl("http://10.0.2.2:8000")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(PizzaApi::class.java)
    }
}