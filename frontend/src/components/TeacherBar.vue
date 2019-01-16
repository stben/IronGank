<template>
  <mu-appbar color="primary" class="bar">
    <mu-button flat slot="left" to="/teacher/index">教师直播系统</mu-button>
    <mu-button flat slot="right" to="/login">退出</mu-button>
    <div style="font-size: 20px">{{title}}</div>
  </mu-appbar>
</template>

<script>
export default {
  name: 'TeacherBar',
  props: ['title']
}
</script>

<style scoped>
  .bar{
    position:fixed;
    width: 100%;
    top: 0;
    left: 0;
  }

</style>
