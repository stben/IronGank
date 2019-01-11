<template>
  <mu-appbar class="bar" color="primary">
    <mu-button flat slot="left" to="/stuIndex">直播系统首页</mu-button>
    {{title}}
    <mu-button flat slot="right" to="/Login">退出</mu-button>
  </mu-appbar>
</template>

<script>
export default {
  name: 'stuBar',
  props: ['title']
}
</script>

<style scoped>
  .bar{
    margin: -60px 0;
  }

</style>
