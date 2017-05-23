package com.fanyafeng.kotlindemo.activity

import android.os.Bundle
import android.support.design.widget.FloatingActionButton
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.GridLayoutManager
import android.support.v7.widget.RecyclerView
import android.support.v7.widget.Toolbar
import android.view.View

import com.fanyafeng.kotlindemo.R
import com.fanyafeng.kotlindemo.BaseActivity
import com.fanyafeng.kotlindemo.adapter.MyListAdapter
import com.fanyafeng.kotlindemo.bean.ListBean

//需要搭配Baseactivity，这里默认为Baseactivity,并且默认BaseActivity为包名的根目录
class ListActivity : BaseActivity() {
    var rvList: RecyclerView? = null
    var listBeanList: MutableList<ListBean> = ArrayList()
    var myListAdapter: MyListAdapter? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list)
        //这里默认使用的是toolbar的左上角标题，如果需要使用的标题为中心的采用下方注释的代码，将此注释掉即可
        title = getString(R.string.title_activity_list)

        initView()
        initData()
    }

    override fun onResume() {
        super.onResume()
        //toolbar_center_title.setText(getString(R.string.title_activity_list));
    }

    //初始化UI控件
    private fun initView() {
        rvList = findViewById(R.id.rvList) as RecyclerView
        rvList!!.layoutManager = GridLayoutManager(this, 2, GridLayoutManager.VERTICAL, false)
        myListAdapter = MyListAdapter(this, listBeanList)
    }

    //初始化数据
    private fun initData() {
        for (i in 0..5) {
            listBeanList.add(ListBean("你好"))
        }
        rvList!!.adapter = myListAdapter

    }

}
