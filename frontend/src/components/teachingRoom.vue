<template>
  <div>
    <stuFrame :selected="''" :title="直播间"></stuFrame>
    <chattingRoom></chattingRoom>
  </div>
</template>

<script>
import stuFrame from './studentFrame'
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
