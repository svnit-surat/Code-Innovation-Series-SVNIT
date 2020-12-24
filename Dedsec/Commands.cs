using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using System.Timers;

namespace _10minstut.Modules
{

    public class Commands : ModuleBase<SocketCommandContext>
    {
        public static Timer SitTimer;
        public static Timer SleepTimer;

        public async void sit_straight_reminder(object obj, ElapsedEventArgs e)
        {
            await ReplyAsync("Sit Straight, you don't want your back to pain when you get old do you?");
        }

        public async void water_reminder(object obj, ElapsedEventArgs e)
        {
            await ReplyAsync("Drink water, you don't want kidney stones do you?  ");
        }

        [Command("Sit")]

        public async Task sitTimer()
        {
            await ReplyAsync("Okay,I will remind you in 15 minutes!");
            System.Timers.Timer SitTimer = new System.Timers.Timer();
            SitTimer.Elapsed += new ElapsedEventHandler(sit_straight_reminder);
            SitTimer.Interval = 900000;
            SitTimer.Enabled = true;
            SitTimer.AutoReset = true;
        }

        [Command("Water")]

        public async Task water()
        {
            await ReplyAsync("Okay,I will remind you in 30 minutes!"); 
            System.Timers.Timer SleepTimer = new System.Timers.Timer();
            SleepTimer.Elapsed += new ElapsedEventHandler(water_reminder);
            SleepTimer.Interval = 1800000;
            SleepTimer.Enabled = true;
            SleepTimer.AutoReset = true;
        }


    }






}
