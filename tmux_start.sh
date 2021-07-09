#!/usr/bin/env bash

sesh="nanopsi"

tmux new-session -d -s $sesh

tmux new-window -t $sesh:1 -n "editor"
tmux send-keys -t "editor" "vim -p *.py" C-m

tmux new-window -t $sesh:2 -n "python3"
tmux send-keys -t "python3" "python3 main.py" C-m

tmux attach-session -t $sesh:1
