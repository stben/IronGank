<template>
  <div>
    <div id="video"
         class="video-div">
      <div id="agora_remote"
           class="remote-div" />
      <div id="agora_local"
           class="local-div" />
    </div>
    <div class="button-div">
      <button id="join"
              class="btn btn-primary"
              @click="join">Join</button>
    </div>
  </div>
</template>

<script>
import AgoraRTC from 'agora-rtc-sdk'
import socket from 'socket.io-client'
const SocketInsatnce = socket('http://localhost:3000')

if (!AgoraRTC.checkSystemRequirements()) {
  alert('Your browser does not support WebRTC!')
}

export default {
  name: 'teacherVideo',
  props: ['stuList', 'roomName', 'roomNo'],
  created: function () {
    SocketInsatnce.emit('joinRoom', this.roomNo)
    SocketInsatnce.emit('updateMyList', this.roomNo)
  },
  methods: {
    join () {
      let self = this
      document.getElementById('join').disabled = true
      let channelKey = null

      console.log('Init AgoraRTC client with App ID: ' + 'a681ef1b092c4e9a801fabdd693830f3')
      let client = AgoraRTC.createClient({ mode: 'live', codec: 'h264' })
      client.init('a681ef1b092c4e9a801fabdd693830f3', function () {
        console.log('AgoraRTC client initialized')
        client.join(channelKey, self.roomNo + 'video', null, function (uid) {
          console.log('User ' + uid + ' join channel successfully')

          let localStream = AgoraRTC.createStream({ streamID: uid, audio: true, video: true, screen: false })
          localStream.on('accessAllowed', function () {
            console.log('accessAllowed')
          })
          localStream.on('accessDenied', function () {
            console.log('accessDenied')
          })
          localStream.init(function () {
            console.log('getUserMedia successfully')
            localStream.play('agora_local')
            const videos = document.querySelectorAll('video')
            for (let i = 0; i < videos.length; i++) {
              videos[i].style.left = '0'
            }
            client.publish(localStream, function (err) {
              console.log('Publish local stream error: ' + err)
            })
            client.on('stream-published', function (evt) {
              console.log('Publish local stream successfully')
            })
          }, function (err) {
            console.log('getUserMedia failed', err)
          })
        }, function (err) {
          console.log('Join channel failed', err)
        })
      }, function (err) {
        console.log('AgoraRTC client init failed', err)
      })
      channelKey = ''
      client.on('error', function (err) {
        console.log('Got error msg:', err.reason)
        if (err.reason === 'DYNAMIC_KEY_TIMEOUT') {
          client.renewChannelKey(channelKey, function () {
            console.log('Renew channel key successfully')
          }, function (err) {
            console.log('Renew channel key failed: ', err)
          })
        }
      })
      client.on('stream-added', function (evt) {
        var stream = evt.stream
        console.log('New stream added: ' + stream.getId())
        console.log('Subscribe ', stream)
        client.subscribe(stream, function (err) {
          console.log('Subscribe stream failed', err)
        })
      })
      client.on('stream-subscribed', function (evt) {
        var stream = evt.stream
        console.log('Subscribe remote stream successfully: ' + stream.getId())
        stream.play('agora_remote')
        const videos = document.querySelectorAll('video')
        for (let i = 0; i < videos.length; i++) {
          videos[i].style.left = '0'
        }
      })
      client.on('stream-removed', function (evt) {
        var stream = evt.stream
        stream.stop()
        console.log('Remote stream is removed ' + stream.getId())
      })
      client.on('peer-leave', function (evt) {
        var stream = evt.stream
        if (stream) {
          stream.stop()
          console.log(evt.uid + ' leaved from this channel')
        }
      })
    }
  }
}
</script>

<style scoped>
.video-div {
  width: 210px;
  height: 294px;
  position: absolute;
  top: 0;
  left: 0;
}
.remote-div {
  width: 210px;
  height: 147px;
  position: absolute;
  top: 0;
  left: 0;
  display: inline-block;
}
.local-div {
  width: 210px;
  height: 147px;
  position: absolute;
  left: 0;
  bottom: 10px;
  display: inline-block;
}
.button-div {
  width: 210px;
  height: 10px;
  position: absolute;
  bottom: 0;
  left: 0;
}
</style>
