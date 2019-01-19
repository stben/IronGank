<template>
  <div>
    <textarea id="code"
              v-model="code"></textarea>
  </div>
</template>

<script>

import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/javascript/javascript.js'
import 'codemirror/theme/blackboard.css'

import socket from 'socket.io-client'
let CodeMirror = require('codemirror/lib/codemirror')
require('codemirror/addon/edit/matchbrackets')
require('codemirror/addon/selection/active-line')
require('codemirror/addon/hint/show-hint.js')
require('codemirror/addon/hint/show-hint.css')
require('codemirror/addon/hint/javascript-hint.js')
const SocketInstance = socket('http://localhost:3000')

export default {
  name: 'codeMirror',
  data () {
    return {
      code: 'Press Ctrl-Space to trigger hint'
    }
  },
  props: ['roomNo', 'status'],
  mounted () {
    let self = this
    SocketInstance.emit('joinRoom', this.roomNo)
    let editor = CodeMirror.fromTextArea(document.getElementById('code'), {
      lineNumbers: true,
      readOnly: this.status,
      styleActiveLine: true,
      matchBrackets: true,
      theme: 'default',
      direction: 'ltr',
      extraKeys: { 'Ctrl-Space': 'autocomplete' }
    })

    SocketInstance.on('getCode', (msg) => {
      alert('getcode!')
      editor.replaceRange(msg.codeMsg, msg.from, msg.to)
    })
    editor.on('change', function (editor, change) {
      if (typeof (change.origin) !== 'undefined') {
        let codedata = {
          'codeMsg': change.text.join('\n'),
          'from': { 'ch': change.from.ch, 'line': change.from.line },
          'to': { 'ch': change.to.ch, 'line': change.to.line }
        }
        let data = { 'roomNo': self.roomNo, 'msg': codedata }
        self.sendCodeMsg(data)
      }
    })
  },

  methods: {
    sendCodeMsg (data) {
      SocketInstance.emit('sendCode', data)
    }
  }
}
</script>

<style>
#code > * {
  text-align: left;
}
</style>
