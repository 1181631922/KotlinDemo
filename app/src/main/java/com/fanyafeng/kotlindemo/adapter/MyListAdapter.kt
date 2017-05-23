package com.fanyafeng.kotlindemo.adapter

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

import com.fanyafeng.kotlindemo.R
import com.fanyafeng.kotlindemo.bean.ListBean

/**
 * Author： fanyafeng
 * Data： 17/5/23 下午4:23
 * Email: fanyafeng@live.cn
 */
class MyListAdapter(private val context: Context, private val listBeanList: List<ListBean>) : RecyclerView.Adapter<MyListAdapter.MyListViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyListViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.item_mylist_layout, parent, false)
        return MyListViewHolder(view)
    }

    override fun onBindViewHolder(holder: MyListViewHolder, position: Int) {
        val listBean = listBeanList[position]
        holder.tvItem!!.text = listBean.title
    }

    override fun getItemCount(): Int {
        return listBeanList.size
    }

    inner class MyListViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var tvItem: TextView? = null

        init {
            tvItem = itemView.findViewById(R.id.tvItem) as TextView
        }
    }

}
