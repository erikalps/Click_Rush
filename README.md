# 🐶 Click Rush

> Jogo de agilidade e reflexo desenvolvido em Python com Pygame. Clique nos beagles antes que eles fujam!

---

## 📋 Sobre o Projeto

**Click Rush** é um jogo acadêmico de clique rápido em que o objetivo é capturar o máximo de beagles possível dentro de **60 segundos**. Os alvos aparecem em posições aleatórias na tela e somem após um curto intervalo — quanto mais difícil a dificuldade, menos tempo você tem!

---

## 🎮 Como Jogar

1. Inicie o jogo e escolha uma dificuldade no menu principal.
2. Clique nos beagles que aparecem na tela antes que eles desapareçam.
3. Cada beagle clicado vale **+1 ponto**.
4. O jogo termina após **60 segundos** — tente fazer o maior score possível!

---

## ⚙️ Dificuldades

| Dificuldade | Intervalo de Spawn | Tempo de Vida do Alvo |
|-------------|-------------------|----------------------|
| Fácil       | 1500ms            | 1500ms               |
| Médio       | 1000ms            | 1000ms               |
| Difícil     | 600ms             | 600ms                |

---

## 🗂️ Estrutura do Projeto

```
Click_Rush/
├── main.py                  # Ponto de entrada do jogo
├── assets/
│   ├── images/
│   │   ├── beagle.png       # Sprite do alvo
│   │   ├── menu2.png        # Fundo do menu e da fase
└── core/
    ├── Const.py             # Constantes globais (cores, dimensões)
    ├── Game.py              # Controlador principal — orquestra Menu e GameScreen
    ├── GameScreen.py        # Lógica da partida (spawn, pontuação, timer)
    ├── Menu.py              # Tela de seleção de dificuldade
    ├── Button.py            # Componente reutilizável de botão
    └── Target.py            # Alvo clicável (beagle)
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- Pygame 2.x

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Click_Rush.git
cd Click_Rush

# Instale a dependência
pip install pygame

# Execute o jogo
python main.py
```

---

## 🛠️ Tecnologias

- **Python 3** — linguagem principal
- **Pygame** — engine gráfica, eventos, áudio e controle de tempo

## 👩‍💻 Autora

Desenvolvido com 🍿 por **[Erika Lopes](https://github.com/erikalps)**
