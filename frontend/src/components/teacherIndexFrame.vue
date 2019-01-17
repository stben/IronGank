<template>
  <div id="teacherIndexFrame">
    <teacherBar v-bind:title="title"></teacherBar>
    <teacherIndexNavigation v-bind:selected="selected"></teacherIndexNavigation>
  </div>
</template>

<script>
import teacherBar from './teacherBar'
import teacherIndexNavigation from '../components/teacherIndexNavigation'
export default {
  name: 'teacherIndexFrame',
  components: {
    teacherBar,
    teacherIndexNavigation
  },
  props: ['selected', 'title']
}
</script>

<style scoped>

</style>
