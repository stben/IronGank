<template>
  <mu-list v-bind:value="selected" class="navigation">
    <mu-list-item button value="0" :to="{ name: 'RoomManage', params: {roomNo: roomNo}}">
      <mu-list-item-title>直播间信息</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="1" :to="{ name: 'PickStuAudit', params: {roomNo: roomNo}}">
      <mu-list-item-title>可排队学生列表</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="2" :to="{ name: 'BanStu', params: {roomNo: roomNo}}">
      <mu-list-item-title>被禁言学生列表</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="3" :to="{ name: 'timeTable', params: {roomNo: roomNo}}">
      <mu-list-item-title>直播间日历</mu-list-item-title>
    </mu-list-item>
  </mu-list>
</template>

<script>
export default {
  name: 'TeacherNavigation',
  props: ['selected', 'roomNo']
}
</script>

<style scoped>
  .navigation{
    width: 200px;
    margin: 60px 0;
  }
</style>
