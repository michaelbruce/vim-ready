" vim-ready
" Author:       Michael Bruce <http://focalpointer.org/>
" Version:      0.1
" " map <Leader>5 :unlet g:loaded_ready<CR>:so %<CR>:echo 'Reloaded!'<CR>

" if exists('g:loaded_ready')
"   finish
" endif

let g:loaded_ready = 1
let s:python_file = expand('<sfile>:p:h') . '/ready.py'

if !has('python')
  finish
else
  python import sys
endif

function! Ready()
  python sys.argv = ['ready']
  exec 'pyfile' . s:python_file
endf

function! Stop()
  python sys.argv = ['stop']
  exec 'pyfile ' . s:python_file
endf

command! Stop call Stop()
command! Ready call Ready()
command! Start call Ready()


