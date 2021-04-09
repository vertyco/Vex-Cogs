from redbot.core.bot import Red

from .core.core import Status

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


def setup(bot: Red) -> None:
    bot.add_cog(Status(bot))
