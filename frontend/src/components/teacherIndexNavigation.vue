<template>
  <mu-list v-bind:value="selected" class="navigation">
    <mu-list-item button value="0" to="/teacher/newRoom">
      <mu-list-item-title>新建房间</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button value="1" to="/student/index">
      <mu-list-item-title>所有房间</mu-list-item-title>
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
