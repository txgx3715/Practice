// pages/home/home.js
Page({
data:{
  num : 0
},
//输入框input事件的执行逻辑
handleInput(e){
  //此处获取了输入源代码输入的数字值
  //console.log(e.detail.value);
 //将input输入的值与data中的数据产生关联
 //正确写法：
this.setData({
  num:e.detail.value
})
},
//加减事件按钮
handletap(e){
  //获取自定义属性operation
  const operation = e.currentTarget.dataset.operation;
  this.setData({
    num:this.data.num + operation
  })
}
 
})