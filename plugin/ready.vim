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
else
  python import sys
endif

function! Ready()
  python sys.argv = ['ready']
  pyfile $HOME/.vim/plugin/vim-ready/ready.py
endf

function! Stop()
  python sys.argv = ['stop']
  pyfile $HOME/.vim/plugin/vim-ready/ready.py
endf

command! Stop call Stop()
command! Ready call Ready()
command! Start call Ready()


