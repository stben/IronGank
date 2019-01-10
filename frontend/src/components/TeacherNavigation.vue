<template>
  <mu-list v-bind:value="selected" class="navigation">
    <mu-list-item button value="0" to="/">
      <mu-list-item-title>直播间信息</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="1" to="/teacher/pickstu/audit">
      <mu-list-item-title>可排队学生列表</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="2" to="/teacher/banstu">
      <mu-list-item-title>被禁言学生列表</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="3" to="/teacher/timeTable">
      <mu-list-item-title>直播间日历</mu-list-item-title>
    </mu-list-item>
  </mu-list>
</template>

<script>
export default {
  name: 'TeacherNavigation',
  props: ['selected']
}
</script>

<style scoped>
  .navigation{
    width: 200px;
    margin: 60px 0;
  }
</style>
