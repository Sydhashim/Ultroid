# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import *


@vc_asst("pause")
async def aoah(e):
    CallsClient.pause_playout()
    await eor(e, "∆ Paused.")


@vc_asst("pause")
async def aoah(e):
    CallsClient.resume_playout()
    await eor(e, "∆ Resumed.")
