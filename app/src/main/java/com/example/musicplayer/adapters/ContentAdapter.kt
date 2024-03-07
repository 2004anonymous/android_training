package com.example.musicplayer.adapters

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.cardview.widget.CardView
import androidx.recyclerview.widget.RecyclerView
import com.example.musicplayer.R
import com.example.musicplayer.models.ContentModel
import kotlin.random.Random

class ContentAdapter(private val context: Context, private val contentList: ArrayList<ContentModel>, val clickListener : OnContentClickListener) : RecyclerView.Adapter<ContentAdapter.MyHolder>() {

    class MyHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val title: TextView = itemView.findViewById(R.id.title);
        val body: TextView = itemView.findViewById(R.id.body);
        val subParent: LinearLayout = itemView.findViewById(R.id.subParent);

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyHolder {
        return MyHolder(LayoutInflater.from(context).inflate(R.layout.content_layout,parent,false))
    }

    override fun getItemCount(): Int {
        return contentList.size
    }

    override fun onBindViewHolder(holder: MyHolder, position: Int) {
        holder.title.text = contentList[position].title
        holder.subParent.setBackgroundColor(getRandomColor())
        holder.itemView.setOnClickListener {
            clickListener.onContentClick()
        }
    }

    private fun getRandomColor():Int{
        val colorList  = ArrayList<Int>()
        colorList.add(R.color.skyBlue)
        colorList.add(R.color.orange)
        colorList.add(R.color.red)
        colorList.add(R.color.black)
        colorList.add(R.color.yellow)
        colorList.add(R.color.green)
        colorList.add(R.color.violet)
        val seed = System.currentTimeMillis().toInt()
        return colorList[Random(seed).nextInt(colorList.size)]
    }
    fun interface OnContentClickListener{
        fun onContentClick()
    }
}