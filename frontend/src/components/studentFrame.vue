<template>
  <div id="studentFrame">
    <studentBar v-bind:title="title"></studentBar>
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
