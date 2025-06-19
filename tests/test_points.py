import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from points import espelhar_ponto, rotacionar_ponto



def test_espelhar_ponto_quadrante_2():
    assert espelhar_ponto(1, 2, 2) == (-1,2)
    
def test_espelhar_ponto_quadrante_3():
    assert espelhar_ponto(1, 2, 3) == (-1,-2)
    
def test_espelhar_ponto_quadrante_4():
    assert espelhar_ponto(1, 2, 4) == (1,-2)
    
def test_espelhar_rotacionar_90():
    assert rotacionar_ponto(1, 2, 90) == (-2.0, 1.0)

def test_espelhar_rotacionar_180():
    assert rotacionar_ponto(1, 2, 180) == (-1.0,-2.0)
    
