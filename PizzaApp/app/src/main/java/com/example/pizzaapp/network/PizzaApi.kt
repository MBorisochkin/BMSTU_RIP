package com.example.pizzaapp.network

import retrofit2.Call
import retrofit2.Response
import retrofit2.http.*

interface PizzaApi { // Инфтерфейс для реализации HTTP-методов

    @GET("/pizza/") // GET-запрос для получения списка всех пицц
    suspend fun getPizzas() : Response<List<Pizza>>

    @FormUrlEncoded
    @POST("/pizza/")  // POST-запрос для добавления пиццы
    fun createPizza(@Field("name") name: String,
                    @Field("topping") topping: String,
                    @Field("diameter") diameter: Int): Call<Pizza>

    @PUT("/pizza/{pk}/") // PUT-запрос для изменения пиццы
    fun updatePizza(@Path("pk") pk: Int, @Body pizza: Pizza): Call<Pizza>

    @DELETE("/pizza/{pk}/") // DELETE-запрос для удаления пиццы
    fun deletePizza(@Path("pk") pk: Int): Call<Pizza>
}