<template>
  <div id="teacherFrame">
    <teacherBar v-bind:title="title"></teacherBar>
    <teacherNavigation v-bind:selected="selected" :roomNo="roomNo"></teacherNavigation>
  </div>
</template>

<script>
import teacherBar from './teacherBar'
import teacherNavigation from './teacherNavigation'
export default {
  name: 'TeacherFrame',
  components: {
    teacherBar,
    teacherNavigation
  },
  props: ['selected', 'title', 'roomNo']
}
</script>

<style scoped>

</style>
