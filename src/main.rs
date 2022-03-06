use std::io::stdin; // Input
use rand::Rng; // Random numbers
use std::{thread, time::Duration}; // For sleeping (Zzz...)

struct Game {
    bot_points: u64,
    player_points: u64,
    current_points: u64,
    minimum: u64,
    maximum: u64,
    limit: u64,
    player_turn: bool,
    turn: u64,
}

impl Game {
    /// Bot's algorithm to get the point
    fn bot_evaluate(&mut self) -> u64 {
        let path = {
            if self.limit % 20 == 0 {
                self.limit / 10 + 1
            } else {
                self.limit / 10
            }
        }; // Path to victory position

        let victory_position = self.limit + path; // Bot will win if it gets this number of points

        let turns_left = self.limit / 10 - 1;

        let mut winning = false;

        let mut final_num = 1u64;

        // Check if a number can add up to victory position
        for num in self.minimum..self.maximum+1 {
            if num + victory_position * (turns_left-self.turn-1) == victory_position {
                winning = true;
                final_num = num;
                break;
            }
        }

        if !winning {
            final_num = rand::thread_rng().gen_range(self.minimum..self.maximum+1);
        }
        self.bot_points = final_num;
        self.current_points += final_num;
        final_num
    }

    fn player_evaluate(&mut self) -> u64 {
        loop {
            println!("Choose a number between {} and {}", self.minimum, self.maximum);
            let input = handle_input().parse::<u64>();
            let mut num = 1u64;

            match input {
                Ok(_v) => { num = input.unwrap(); },
                _ => continue,
            }

            if num < self.minimum || num > self.maximum { continue; }

            self.player_points = num;
            break;
        }
        self.player_points
    }

    fn bot_play(&mut self) {
        println!("Bot's turn!");
        println!("Bot choose {}", self.bot_evaluate());
        self.player_turn = true;

    }

    fn player_play(&mut self) {
        println!("Player's turn!");
        println!("Player choose {}", self.player_evaluate());
        self.player_turn = false;
    }

    /// Print the winner
    fn get_winner(&mut self) {
        if self.player_turn {
            println!("Player wins!");
        } else {
            println!("Bot wins!");
        }
    }

    /// Run the game
    fn play(&mut self) -> () {
        while self.current_points < self.limit {
            let mut turns = 0;
            self.turn += 1;
            println!("Turn: {}", self.turn);
            println!("Current points: {}", self.current_points);

            while turns < 2 {
                if self.player_turn {
                    self.player_play();
                } else {
                    self.bot_play();
                }
                turns += 1;
            }
        }
        self.get_winner();
        thread::sleep(Duration::from_millis(3000));
    }


}

fn handle_input() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap().to_string()
}

fn main_menu() -> () {
    let mut game = Game {
        bot_points: 0,
        player_points: 0,
        current_points: 0,
        limit: 100,
        minimum: 1,
        maximum: 10,
        player_turn: false,
        turn: 0,
    };

    loop {
        println!("
Welcome to The Game You Always Lose!

1) AI go first
2) You go first
3) Exit
        ");

        // let input: u8 = buf.trim().parse().unwrap();
        let input = handle_input();
        println!("{:?} {}", input.trim().parse::<u8>(), input);

        match input.trim().parse() {
            Ok(2) => game.play(),
            Ok(3) => std::process::exit(1),
            _ => println!("Invaild input!"),
        }; 
    }
}

fn main() {
    main_menu();
}
