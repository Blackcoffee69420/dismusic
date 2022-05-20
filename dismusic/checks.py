from discord.ext import commands
import nextcord

from .errors import MustBeSameChannel, NotConnectedToVoice, PlayerNotConnected


def voice_connected():
    def predicate(ctx: commands.Context):
        em=nextcord.Embed(title="Error",description="You are not connected to any voice channel.")
        if not ctx.author.voice:
            raise NotConnectedToVoice(embed=em)

        return True

    return commands.check(predicate)


def voice_channel_player():
    def predicate(ctx: commands.Context):
        if not ctx.author.voice:
            em=nextcord.Embed(title="Error",description="You are not connected to any voice channel.")
            raise NotConnectedToVoice(embed=em)

        if not ctx.voice_client:
            em=nextcord.Embed(title="Error",description="Player is connected to any voice channel.")
            raise PlayerNotConnected(embed=em)

        if ctx.voice_client.channel.id != ctx.author.voice.channel.id:
            em=nextcord.Embed(title="Error",description="You must be in the same voice channel as the player.")
            raise MustBeSameChannel(embed=em)

        return True

    return commands.check(predicate)
