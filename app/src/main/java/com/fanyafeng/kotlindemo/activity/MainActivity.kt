package com.fanyafeng.kotlindemo.activity

import android.os.Bundle
import android.support.design.widget.FloatingActionButton
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.Toolbar
import android.view.View
import android.widget.Button
import android.widget.TextView

import com.fanyafeng.kotlindemo.R
import com.fanyafeng.kotlindemo.BaseActivity
import com.fanyafeng.kotlindemo.R.id.btnShow1

//需要搭配Baseactivity，这里默认为Baseactivity,并且默认BaseActivity为包名的根目录
class MainActivity : BaseActivity(), View.OnClickListener {
    val a: Int = 1
    var btnShow1: Button? = null
    var tvShow: TextView? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //这里默认使用的是toolbar的左上角标题，如果需要使用的标题为中心的采用下方注释的代码，将此注释掉即可
        title = getString(R.string.title_activity_main)
        isSetNavigationIcon = false

        initView()
        initData()
    }

    override fun onResume() {
        super.onResume()
        //toolbar_center_title.setText(getString(R.string.title_activity_main));
    }

    //初始化UI控件
    private fun initView() {
        btnShow1 = findViewById(R.id.btnShow1) as Button
        btnShow1!!.setOnClickListener(this)
        tvShow = findViewById(R.id.tvShow) as TextView
    }

    //初始化数据
    private fun initData() {
//        btnShow1!!.setOnClickListener { tvShow!!.text = "你好" }
    }

    override fun onClick(v: View) {
        when (v) {
            btnShow1 -> {
                tvShow!!.text = "你好"
            }
        }
    }

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

}
