<template>
  <div id="teacherNavigation">
    <mu-paper :z-depth="3" class="paper">
      <mu-list v-bind:value="selected">
        <mu-list-item button value="0" :to="{ name: 'roomManage', params: {roomNo: roomNo}}">
          <mu-list-item-title class="title">直播间信息</mu-list-item-title>
        </mu-list-item>
        <mu-list-item button value="1" :to="{ name: 'pickStuAudit', params: {roomNo: roomNo}}">
          <mu-list-item-title class="title">可排队学生列表</mu-list-item-title>
        </mu-list-item>
        <mu-list-item button value="2" :to="{ name: 'banStu', params: {roomNo: roomNo}}">
          <mu-list-item-title class="title">被禁言学生列表</mu-list-item-title>
        </mu-list-item>
        <mu-list-item button value="3" :to="{ name: 'pickTeacherAudit', params: {roomNo: roomNo}}">
          <mu-list-item-title class="title">助教列表</mu-list-item-title>
        </mu-list-item>
        <mu-list-item button value="4" :to="{ name: 'timeTable', params: {roomNo: roomNo}}">
          <mu-list-item-title class="title">直播间日历</mu-list-item-title>
        </mu-list-item>
      </mu-list>
      <mu-list>
        <mu-list-item button value="0" to="/teacher/index" class="return">
          <mu-list-item-title class="title">返回首页</mu-list-item-title>
        </mu-list-item>
      </mu-list>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'teacherNavigation',
  props: ['selected', 'roomNo']
}
</script>

<style scoped>
  .paper{
    position: fixed;
    width: 200px;
    height: 100%;
    top: 60px;
    left: 0;
  }
  .title{
    font-size: 13px;
  }
  .return{
    margin-top: 400px;
  }
</style>
