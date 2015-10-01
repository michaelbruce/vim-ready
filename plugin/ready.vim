" vim-ready
" Author:       Michael Bruce <http://focalpointer.org/>
" Version:      0.1
" " map <Leader>5 :unlet g:loaded_ready<CR>:so %<CR>:echo 'Reloaded!'<CR>

" if exists('g:loaded_ready')
"   finish
" endif

let g:loaded_ready = 1

if !has('python')
  finish
endif

function! Ready()
  python import sys
  python sys.argv = ['ready']
  pyfile %:h/ready.py
endf

command! Ready call Ready()
command! Start call Ready()

function! Stop()
  python import sys
  python sys.argv = ['stop']
  pyfile %:h/ready.py
endf

command! Stop call Stop()

