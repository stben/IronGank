<template>
  <mu-appbar class="bar" color="primary">
    <mu-button flat slot="left" to="/teacher/index">教师直播系统</mu-button>
    <mu-button flat slot="right" to="/login">退出</mu-button>
    {{title}}
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
    margin: -60px 0;
  }

</style>
