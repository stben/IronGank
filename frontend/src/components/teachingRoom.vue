<template>
  <div>
    <stuFrame :selected="''" :title="'学生 '+stuNo+''"></stuFrame>
    <chattingRoom></chattingRoom>
  </div>
</template>

<script>
import stuFrame from '../components/stuFrame'
import chattingRoom from '../components/chattingRoom'
export default {
  name: 'teachingRoom',
  components: {
    stuFrame,
    chattingRoom
  }
}
</script>

<style scoped>

</style>
