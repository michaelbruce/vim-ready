" vim-ready
" Author:       Michael Bruce <http://focalpointer.org/>
" Version:      0.1

if exists('g:loaded_ready')
  finish
endif

let g:loaded_ready = 1
let s:python_file = expand('<sfile>:p:h') . '/ready.py'

if !has('python')
  finish
else
  python import sys; sys.argv = ['stop']
endif

function! ToggleReady()
  python << EOF
if sys.argv == ['stop']:
    sys.argv = ['ready']
else:
    sys.argv = ['stop']
EOF
  exec 'pyfile' . s:python_file
endf

function! Ready()
  python sys.argv = ['ready']
  exec 'pyfile' . s:python_file
endf

function! Stop()
  python sys.argv = ['stop']
  exec 'pyfile ' . s:python_file
endf

command! Stop call Stop()
command! ToggleReady call ToggleReady()
command! Start call Ready()
command! Toggle call Toggle()
