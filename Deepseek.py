from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import moviepy.editor as mp
from config import TOKEN

def start(update, context):
    update.message.reply_text("👋 Hello! I'm DeepSeek AI Video Editor Bot 🎬🔥")

def handle_video(update, context):
    video_file = update.message.video
    new_file = context.bot.get_file(video_file.file_id)
    new_file.download('input_video.mp4')

    # Auto Shake Effect
    clip = mp.VideoFileClip("input_video.mp4")
    final_clip = clip.fx(mp.vfx.lum_contrast, 1.5, 10)
    final_clip.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

    context.bot.send_video(chat_id=update.message.chat_id, video=open("output_video.mp4", "rb"))

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.video, handle_video))

updater.start_polling()
