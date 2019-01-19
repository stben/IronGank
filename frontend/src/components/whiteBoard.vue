<template>
  <div>
    <canvas class='whiteboard'
            name='whiteboard'></canvas>
    <div class='colors'>
      <el-color-picker v-model='color'></el-color-picker>
      <div :class='{tool:true, delete:true, "black-background": isBlack, "white-background": !isBlack}'></div>
      <div :class='{tool:true, rectanger:true, "blue-background": drawRec, "white-background": !drawRec}'></div>
    </div>
  </div>
</template>

<script>
import socket from 'socket.io-client'
const SocketInstance = socket('http://localhost:3000')
export default {
  name: 'WhiteBoard',
  data () {
    return {
      isBlack: false,
      drawRec: false,
      CRASHCAN_NUM: 0,
      DRAW_REC: 1,
      color: '#111111',
      canvas: null,
      context: null,
      current: { color: 'black' },
      drawing: false
    }
  },
  props: ['roomNo'],
  mounted () {
    SocketInstance.emit('joinRoom', this.roomNo)
    this.canvas = document.getElementsByClassName('whiteboard')[0]
    this.context = this.canvas.getContext('2d')
    this.canvas.width = 855
    this.canvas.height = 310
    this.canvas.addEventListener('mousedown', this.onMouseDown, false)
    this.canvas.addEventListener('mouseup', this.onMouseUp, false)
    this.canvas.addEventListener('mouseout', this.onMouseUp, false)
    this.canvas.addEventListener(
      'mousemove',
      this.throttle(this.onMouseMove, 10),
      false
    )
    let crashCan = document.getElementsByClassName('tool')[this.CRASHCAN_NUM]
    crashCan.addEventListener('mousedown', this.onReadyClear, false)
    crashCan.addEventListener('mouseup', this.onClear, false)
    let drawRec = document.getElementsByClassName('tool')[this.DRAW_REC]
    drawRec.addEventListener('mouseup', this.onChangeDrawRec, false)
    SocketInstance.on('drawing', this.onDrawingEvent)
    SocketInstance.on('clear', this.onClearEvent)
    SocketInstance.on('drawRec', this.onDrawRecEvent)
  },
  methods: {
    onChangeDrawRec: function () {
      this.drawRec = !this.drawRec
    },
    onReadyClear: function () {
      this.isBlack = true
    },
    onClear: function () {
      this.isBlack = false
      this.canvas.width = 855
      this.canvas.height = 310
      SocketInstance.emit('clear', false)
    },

    onClearEvent: function () {
      this.canvas.width = 855
      this.canvas.height = 310
    },
    drawLine: function (x0, y0, x1, y1, color, needEmit) {
      this.context.moveTo(x0 - 210, y0 - 360)
      this.context.lineTo(x1 - 210, y1 - 360)
      this.context.strokeStyle = color
      this.context.lineWidth = 2
      this.context.stroke()
      if (!needEmit) {
        return
      }
      SocketInstance.emit('drawing', {
        x0: x0,
        y0: y0,
        x1: x1,
        y1: y1,
        color: color
      })
    },
    drawRectang: function (x0, y0, x1, y1, color, needEmit) {
      this.context.fillStyle = color
      this.context.fillRect(x0 - 210, y0 - 360, x1 - x0, y1 - y0)
      if (!needEmit) {
        return
      }
      SocketInstance.emit('drawRec', {
        x0: x0,
        y0: y0,
        x1: x1,
        y1: y1,
        color: color
      })
    },
    onMouseDown: function (e) {
      console.log('mouse down')
      if (this.drawRec && this.drawing) {
        return
      }
      this.current.x = e.clientX
      this.current.y = e.clientY
      this.drawing = true
    },
    onMouseUp: function (e) {
      console.log('mouse up')
      if (!this.drawing) {
        return
      }
      this.drawing = false
      if (this.drawRec) {
        this.drawRectang(
          this.current.x,
          this.current.y,
          e.clientX,
          e.clientY,
          this.color,
          true
        )
        return
      }
      this.drawLine(
        this.current.x,
        this.current.y,
        e.clientX,
        e.clientY,
        this.color,
        true
      )
    },
    onMouseMove: function (e) {
      if (!this.drawing) {
        return
      }
      if (this.drawRec) {
        this.drawRectang(
          this.current.x,
          this.current.y,
          e.clientX,
          e.clientY,
          this.color,
          true
        )
        return
      }
      this.drawLine(
        this.current.x,
        this.current.y,
        e.clientX,
        e.clientY,
        this.color,
        true
      )
      this.current.x = e.clientX
      this.current.y = e.clientY
    },

    onColorUpdate: function (e) {
      this.current.color = this.color
    },
    throttle: function (callback, delay) {
      let previousCall = new Date().getTime()
      return function () {
        let time = new Date().getTime()

        if (time - previousCall >= delay) {
          previousCall = time
          callback.apply(null, arguments)
        }
      }
    },
    onDrawingEvent: function (data) {
      this.drawLine(
        data.x0,
        data.y0,
        data.x1,
        data.y1,
        data.color
      )
    },
    onDrawRecEvent: function (data) {
      this.drawRectang(
        data.x0,
        data.y0,
        data.x1,
        data.y1,
        data.color
      )
    }
  },
  watch: {}
}
</script>

<style scoped>
.one-div {
  height: 65vh;
  width: 56vw;
  margin: 0 auto;
  padding: 0;
}

.whiteboard {
  position: fixed;
  top: 360px;
  left: 210px;
  width: 855px;
  height: 310px;
  margin: 0 auto;
}

.colors {
  position: fixed;
}

.tool {
  display: inline-block;
  height: 48px;
  width: 48px;
}

.tool.delete {
  background-image: url(../assets/trash-can.png);
  background-repeat: no-repeat;
  background-position: center;
}

.tool.rectanger {
  background-image: url(../assets/rectanger.png);
  background-repeat: no-repeat;
  background-position: center;
}

.black-background {
  background-color: #555555;
}

.white-background {
  background-color: #ffffff;
}

.blue-background {
  background-color: #0ff8f0;
}

.color {
  display: inline-block;
  height: 48px;
  width: 48px;
}
</style>
