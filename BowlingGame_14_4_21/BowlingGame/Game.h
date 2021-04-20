class Game {
  int val;
public:
  Game();
  int getVal() { return this->val; }

};


Game::Game() : val(1)
{
}