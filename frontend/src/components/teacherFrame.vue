<template>
  <div id="teacherFrame">
    <TeacherBar v-bind:title="title"></TeacherBar>
    <TeacherNavigation v-bind:selected="selected" :roomNo="roomNo"></TeacherNavigation>
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
