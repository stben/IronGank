<template>
  <div id="stuFrame">
    <stuBar v-bind:title="title"></stuBar>
  </div>
</template>

<script>
import stuBar from '../components/stuBar'
export default {
  name: 'stuFrame',
  components: {
    stuBar
  },
  props: ['selected', 'title']
}
</script>

<style scoped>

</style>
