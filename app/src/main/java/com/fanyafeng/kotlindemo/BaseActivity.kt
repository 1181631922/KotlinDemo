package com.fanyafeng.kotlindemo

import android.os.Bundle
import android.widget.TextView
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.Toolbar
import android.view.View
import android.view.Menu
import android.view.MenuItem

open class BaseActivity : AppCompatActivity(), View.OnClickListener {

    protected var toolbar: Toolbar? = null
    protected var toolbar_center_title: TextView? = null
    protected var isShowToolbar = true
    protected var isSetNavigationIcon = true
    protected var isSetLogo = false
    protected var isShowEmail = true
    protected var title: String? = null
    protected var centertitle: String? = null
    protected var subtitle: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onClick(v: View) {

    }

    override fun onResume() {
        super.onResume()
        toolbar = findViewById(R.id.toolbar) as Toolbar
        toolbar_center_title = findViewById(R.id.toolbar_center_title) as TextView
        if (toolbar != null) {
            if (isShowToolbar) {
                setSupportActionBar(toolbar)
            } else {
                toolbar!!.visibility = View.GONE
            }

            if (title != null && title != "") {
                toolbar!!.title = title
            } else {
                toolbar!!.title = ""
            }

            if (subtitle != null && subtitle != "") {
                toolbar!!.subtitle = subtitle
            }
            if (isSetNavigationIcon) {
                //                由于要兼容低版本，所以采用这个划杠的方法，需要自己根据需求替换图片
                toolbar!!.navigationIcon = resources.getDrawable(R.drawable.back)
                toolbar!!.setNavigationOnClickListener { finish() }
            }
            if (isSetLogo) {
                //需要自己根据需求进行替换图片
                toolbar!!.logo = resources.getDrawable(R.mipmap.ic_launcher)
            }

            if (toolbar_center_title != null) {
                if (centertitle != null && centertitle != "") {
                    toolbar_center_title!!.text = centertitle
                } else {
                    toolbar_center_title!!.text = ""
                }

            }

        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_base, menu)
        //        默认隐藏setting按钮
        if (toolbar != null) {
            val menuItem = toolbar!!.menu.getItem(0)
            if (menuItem != null) {
                menuItem.isVisible = false
            }
        }
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {

        val id = item.itemId

        when (id) {
            R.id.action_settings -> {
            }
        }

        return super.onOptionsItemSelected(item)
    }
}
