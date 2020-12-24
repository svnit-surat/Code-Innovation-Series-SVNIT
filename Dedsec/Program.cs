using System;
using System.Reflection;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using Microsoft.Extensions.DependencyInjection;

namespace _10minstut
{
    class Program
    {
        static void Main(string[] args) => new Program().RunBotAsync().GetAwaiter().GetResult();
        public String time;
        public String time_1;
        private DiscordSocketClient _client;
        private CommandService _commands;
        private IServiceProvider _services;

        public async Task RunBotAsync()
        {
            _client = new DiscordSocketClient();
            _commands = new CommandService();
            _services = new ServiceCollection()
                .AddSingleton(_client)
                .AddSingleton(_commands)
                .BuildServiceProvider();



            string token = "NzkwNzc3NTgzNjU0MjczMDM0.X-FjAw.iORGOPqVhE0gfbd_UOU26YULGAE";

            _client.Log += _client_Log;

            await RegisterCommandsAsync();

            await _client.LoginAsync(TokenType.Bot, token);

            await _client.StartAsync();

            await Task.Delay(-1);

        }

        private Task _client_Log(LogMessage arg)
        {
            Console.WriteLine(arg);
            return Task.CompletedTask;
        }

        public async Task RegisterCommandsAsync()
        {
            _client.MessageReceived += HandleCommandAsync;
            await _commands.AddModulesAsync(Assembly.GetEntryAssembly(), _services);
        }



        private async Task HandleCommandAsync(SocketMessage arg)
        {
            var message = arg as SocketUserMessage;
            var context = new SocketCommandContext(_client, message);
            if (message.Author.IsBot) return;

            int argPos = 0;
            if (message.HasStringPrefix("*", ref argPos))
            {
                var result = await _commands.ExecuteAsync(context, argPos, _services);
                if (!result.IsSuccess) Console.WriteLine(result.ErrorReason);
                if (result.Error.Equals(CommandError.UnmetPrecondition)) await message.Channel.SendMessageAsync(result.ErrorReason);
            }



            if (arg.Content.StartsWith("*Sleep"))
            {
                time = arg.Content.ToLower();
                time_1 = time.Replace("*sleep", "");
                await arg.Channel.SendMessageAsync("I will remind you in " + time_1 + " minutes!");
                Console.WriteLine(time_1);
                int time_int = int.Parse(time_1);

                time_int *= 60000;
                System.Threading.Thread.Sleep(time_int);

                await arg.Channel.SendMessageAsync(arg.Author.Mention + " Sleep,Wasn't that your last game?");

            }

        }

    }
}
