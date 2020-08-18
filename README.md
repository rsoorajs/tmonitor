# tmonitor [![License](https://img.shields.io/badge/License-AGPLv3-green)](https://img.shields.io/badge/License-AGPLv3-green) 
A telegram userbot made with Pyrogram to monitor messages from someone and forward them automatically to someone else

## Installation

At least python 3.6 and Pyrogram version 0.18.0.
I also suggest to install the optional dependency tgcrypto

```bash
python3 -m pip install --user pyrogram tgcrypto
```

## Usage

To start it you have to fill the entries in the `settings.config` file.

*Note:* You can get api\_id and api\_hash at my.telegram.org

After you've inserted all the data, you have to start the main.py file and it will send you a confirmation code.

When the userbot is up and running you can do the following things

You can start monitoring people by doing sending those commands in telegram:

* `.monitor username` to start monitoring someone by username
* `.monitor chat_id` to start monitoring someone by chat id
* `.m username` same as `.monitor username`
* `.m chat_id` same as `m chat_id`

Sending `.monitor` or `.m` without any arguments will automatically add that chat's chat id to the monitor list.

To see the list of monitored people you can use `.monitor_list` or `.m_list`.

To clear the list of monitored people you can use `.monitor_clear` or `m_clear`.

The monitor list can be found in the `monitor.list` file which will be automatically created once you add someone to the list

*Note:* commands will not work in a monitored chat, so please use your private chat or any other to send commands once you've start monitoring someone.



Now that you know how to add people to the monitor list let's see how you forward stuff.

To forward stuff to a channel/group/chat has to be in the forward list.

You can add entries to the forward list by doing:

* `.forward username` to add username to the forwarding list
* `.fwd username` same as `.forward username`

As you've noticed, I decided to not support chad ids here.

To see the forward list you can do `.forward_list` or `.fwd_list`

To clear the forward list you can do `.forward.clear` or `.fwd_clear`

The forward list can be found in the `forward.list` file which will be automatically created once you add an entry



*Note:* I'm assuming you are using the default command prefix ".", but if you changed it, change the commands you see in this guide with the ones that work for you.
