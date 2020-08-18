#************************************** 
#
#     Copyright 2020 Massimiliano Noviello <massi.noviello@gmail.com>
#
#     Use, modification, and distribution of this software
#     are protected by the 
#     GNU AFFERO GENERAL PUBLIC LICENSE Version 3
#     as known as AGPLv3
#
#     The terms of AGPLv3 apply
#
#
#**************************************

from pyrogram import Client, Filters

def save_list(to_save):
    if to_save == "monitor" or to_save == "m":
        to_save = ["monitor", monitor_list]
    elif to_save == "monitor_chat" or to_save == "mc":
        to_save = ["monitor_chat", mc_list]
    elif to_save == "forward" or to_save == "fwd":
        to_save = ["forward", forward_list]
    else:
        raise ValueError

    with open(to_save[0]+".list", "w") as f:
        f.write("\n".join([str(x) for x in to_save[1]])+"\n")

def load_list(to_load):

    if not to_load.endswith(".list"): to_load = to_load + ".list"

    if to_load == "monitor.list" or to_load == "m.list":
        to_load = "monitor.list"
    elif to_load == "monitor_chat.list" or to_load == "mc.list":
        to_load = "monitor_chat.list"
    elif to_load == "forward.list" or to_load == "fwd.list":
        to_load = "forward.list"
    else:
        raise ValueError

    try:
        with open(to_load, "r") as f:

            if f.read().replace("\n","") == "":
                return []
            else:

                to_return = []

                for x in f.readlines():
                    x = x.replace("\n", "")
                    if x.isdigit():
                        to_return.append(int(x))
                    elif x[0] == "-" and x[:1].isdigit():
                        to_return.append(int(x))
                    elif x[0].isdigit() and not x[1:].isdigit():
                        pass
                    else:
                        to_return.append(x)

                return to_return


    except FileNotFoundError:
        return []




##### load settings
with open("settings.conf", "r") as f:
    data = f.readlines()

[data.remove(x) for x in data if x == "\n"]
data = [x.replace("\n", "") for x in data]

data = [x.split("#")[0] for x in data]

data = [x.split("=") for x in data]

settings = {}

for x, y in data:
    y = y.strip()
    if y.isdigit(): y = int(y)
    settings[x] = y

if settings["command_prefix"] == "\eq": settings["command_prefix"] = "="
#####


monitor_list = load_list("m")

mc_list = load_list("mc")

forward_list = load_list("fwd")


app = Client("profile",
        api_id=settings["api_id"],
        api_hash=settings["api_hash"],
        phone_number=settings["phone_number"]
        )

try:

    @app.on_message(Filters.me & Filters.command(["monitor", "m"], settings["command_prefix"]))
    def monitoradd(client, message):
        global monitor_list

        if len(message.text.split()) == 1:
            if message.chat.id in monitor_list:
                message.reply("No duplicates")
            else:
                monitor_list.append(message.chat.id)
                save_list("m")
                message.reply("Ok")


        else:
            name = message.text.split()[1]
            if name.isdigit():
                name = int(name)
                if name in monitor_list:
                    message.reply("No duplicates")
                else:
                    monitor_list.append(name)
                    save_list("m")
                    message.reply("Ok")

            elif name[0].isdigit() and name[1:].isdigit() == False:
                message.reply("Invalid name")

            else:
                if name in monitor_list:
                    message.reply("No duplicates")
                else:
                    monitor_list.append(name)
                    save_list("m")
                    message.reply("Ok")

    @app.on_message(Filters.me & Filters.command(["monitor_chat", "mc"], settings["command_prefix"]))
    def mcadd(client, message):
        global mc_list

        if len(message.text.split()) == 1:
            if message.chat.id in mc_list:
                message.reply("No duplicates")
            else:
                mc_list.append(message.chat.id)
                save_list("mc")
                message.reply("Ok")


        else:
            name = message.text.split()[1]
            if name.isdigit():
                name = int(name)
                if name in mc_list:
                    message.reply("No duplicates")
                else:
                    mc_list.append(name)
                    save_list("mc")
                    message.reply("Ok")

            elif name[0] == "-" and name[1:].isdigit():
                name = int(name)
                if name in mc_list:
                    message.reply("No duplicates")
                else:
                    mc_list.append(name)
                    save_list("mc")
                    message.reply("Ok")


            elif name[0].isdigit() and name[1:].isdigit() == False:
                message.reply("Invalid name")

            else:
                if name in mc_list:
                    message.reply("No duplicates")
                else:
                    mc_list.append(name)
                    save_list("mc")
                    message.reply("Ok")

    @app.on_message(Filters.me & Filters.command(["forward", "fwd"], settings["command_prefix"]))
    def fwdadd(client, message):
        global forward_list

        if len(message.text.split()) == 1:
            message.reply("Not enough args")

        else:
            forward_list.append(message.text.split()[1])
            save_list("fwd")
            message.reply("Ok")


    @app.on_message(Filters.me & Filters.command(["forward_list", "fwd_list"], settings["command_prefix"]))
    def fwdlist(client, message):
        message.reply(f"Forward list:\n{forward_list}")

    @app.on_message(Filters.me & Filters.command(["monitor_list", "m_list"], settings["command_prefix"]))
    def monitorlist(client, message):
        message.reply(f"Monitor list:\n{monitor_list}")

    @app.on_message(Filters.me & Filters.command(["monitor_chat_list", "mc_list"], settings["command_prefix"]))
    def mclist(client, message):
        message.reply(f"Monitor chat list:\n{mc_list}")

    @app.on_message(Filters.me & Filters.command(["monitor_clear", "m_clear"], settings["command_prefix"]))
    def monitorclear(client, message):
        global monitor_list
        message.reply(f"Cleared {len(monitor_list)} from monitor_list")
        monitor_list = []
        save_list("m")

    @app.on_message(Filters.me & Filters.command(["monitor_chat_clear", "mc_clear"], settings["command_prefix"]))
    def mcclear(client, message):
        global mc_list
        message.reply(f"Cleared {len(mc_list)} from monitor_list")
        mc_list = []
        save_list("m")

    @app.on_message(Filters.me & Filters.command(["forward_clear", "fwd_clear"], settings["command_prefix"]))
    def fwdclear(client, message):
        global forward_list
        message.reply(f"Cleared {len(forward_list)} from forward_list")
        forward_list = []
        save_list("fwd")

    @app.on_message(Filters.create(lambda _, x: x.chat.username in mc_list or x.chat.id in mc_list)) # Using Filters.create instead of Filters.chat so I can update the list dynamically
    def cfwd(client, message):
        for chat in forward_list:
            message.forward(f"@{chat}")

    @app.on_message(Filters.create(lambda _, x: x.from_user.username in monitor_list or x.from_user.id in monitor_list)) # Using Filters.create instead of Filters.chat so I can update the list dynamically
    def fwd(client, message):
        for chat in forward_list:
            message.forward(f"@{chat}")

except Exception as e:
    print("\n<<----------------BEGIN-ERROR----------------\n", e, "\n------------------END-ERROR---------------->>\n")


app.run()
