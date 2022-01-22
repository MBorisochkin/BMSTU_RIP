package com.example.pizzaapp.network

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.AsyncListDiffer
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.RecyclerView
import com.example.pizzaapp.databinding.ItemViewBinding

class PizzaAdapter: RecyclerView.Adapter<PizzaAdapter.PizzaViewHolder>() { // Адаптер для RecyclerView

    private lateinit var mListener : onItemClickListener

    interface onItemClickListener{ // Интерфейс обратоки события нажатия на ViewHolder

        fun onItemClick(position: Int)

    }

    fun setOnItemClickListener(listener: onItemClickListener) { // Подписка на обработку события нажатия кнопки
        mListener = listener
    }

    inner class PizzaViewHolder(val binding: ItemViewBinding, listener: onItemClickListener) : RecyclerView.ViewHolder(binding.root) { // ViewHolder для пиццы
        init {
            itemView.setOnClickListener{
                listener.onItemClick(adapterPosition)
            }
        }
    }

    private val diffCallback = object : DiffUtil.ItemCallback<Pizza>() {
        override fun areItemsTheSame(oldItem: Pizza, newItem: Pizza): Boolean { // Реализация метода areItemsTheSame
            return oldItem.pk == newItem.pk
        }

        override fun areContentsTheSame(oldItem: Pizza, newItem: Pizza): Boolean { // Реализация метода areContentsTheSame
            return oldItem == newItem
        }
    }

    private val differ = AsyncListDiffer(this, diffCallback)
    var pizzas: List<Pizza>
    get() = differ.currentList
    set(value) { differ.submitList(value) }

    override fun getItemCount(): Int = pizzas.size // Реализация метода getItemCount

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PizzaViewHolder { // Реализация метода onCreateViewHolder
        return  PizzaViewHolder(ItemViewBinding.inflate(LayoutInflater.from(parent.context),
            parent, false), mListener)
    }

    override fun onBindViewHolder(holder: PizzaViewHolder, position: Int) { // Реализация метода onBindViewHolder
        holder.binding.apply {
            val pizza = pizzas[position]
            itemText.text = pizza.name
        }
    }
}