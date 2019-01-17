<template>
  <div id="studentFrame">
    <stuBar v-bind:title="title"></stuBar>
  </div>
</template>

<script>
import studentBar from './studentBar'
export default {
  name: 'stuFrame',
  components: {
    studentBar
  },
  props: ['selected', 'title']
}
</script>

<style scoped>

</style>
