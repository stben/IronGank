<template>
  <div>
    <stuFrame :selected="''" :title="直播间"></stuFrame>
    <chattingRoom></chattingRoom>
    <codemirror :roomNo='123' v-bind:status="status"/>
  </div>
</template>

<script>
import stuFrame from './studentFrame'
import chattingRoom from '../components/chattingRoom'
import codemirror from '../components/codemirror'
export default {
  name: 'teachingRoom',
  components: {
    stuFrame,
    chattingRoom,
    codemirror,
  },
  data(){
    return{
      status:false
    }
  }
}
</script>

<style scoped>

</style>
