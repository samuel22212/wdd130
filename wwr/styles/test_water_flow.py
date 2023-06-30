from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe,pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
def test_water_column_height():
    water_height = water_column_height(0,0)
    assert water_height == 0

    water_height2 = water_column_height(0,10)
    assert water_height2 == 7.5

    water_height3 = water_column_height(25,0)
    assert water_height3 == 25

    water_height4 = water_column_height(48.3,12.8)
    assert water_height4 == 57.9

def test_pressure_gain_from_water_height():
    pressure1 = pressure_gain_from_water_height(0)
    assert pressure1 == 0
    pressure2 = pressure_gain_from_water_height(30.2)
    pressure3 = pressure_gain_from_water_height(50)
    assert pressure2 == pytest.approx(295.628,0.001)
    assert pressure3 == pytest.approx(489.450, 0.001)

def test_pressure_loss_from_pipe():
    pressure_loss1 = pressure_loss_from_pipe(0.048692,0,0.018,1.75)
    pressure_loss2 = pressure_loss_from_pipe(0.048692,200,0,1.75)
    pressure_loss3 = pressure_loss_from_pipe(0.048692,200,0.018,0)
    assert pressure_loss1 == 0
    assert pressure_loss2 == 0
    assert pressure_loss3 == 0
    pressure_loss = pressure_loss_from_pipe(0.048692,200,0.018,1.75)
    assert pressure_loss == pytest.approx(-113.008, 0.001)

def test_pressure_loss_from_fittings():
    pressure_loss1 = pressure_loss_from_fittings(0,3)
    pressure_loss2 = pressure_loss_from_fittings(1.65,0)
    assert pressure_loss1 == 0
    assert pressure_loss2 == 0
    pressure_loss3 = pressure_loss_from_fittings(1.65,2)
    assert pressure_loss3 == pytest.approx(-0.109, 0.001)
    pressure_loss4 = pressure_loss_from_fittings(1.75, 2)
    assert pressure_loss4 == pytest.approx(-0.122, 0.001)

def test_reynolds_number():
    reynolds1 = reynolds_number(0.048692,0)
    reynolds2 = reynolds_number(0.048692,1.65)
    reynolds3 = reynolds_number(0.048692,1.75)
    reynolds4 = reynolds_number(0.28687,1.65)
    reynolds5 = reynolds_number(0.28687,1.75)
    assert reynolds1 == 0 
    assert  reynolds2 == pytest.approx(80069,1)
    assert  reynolds3 == pytest.approx(84922,1)
    assert  reynolds4 == pytest.approx(471729,1)
    assert  reynolds5 == pytest.approx(500318,1)

def test_pressure_loss_from_pipe_reduction():
    pressure1 = pressure_loss_from_pipe_reduction(0.28687,0,1,0.048692)
    pressure2 = pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692)


pytest.main(["-v", "--tb=line", "-rN", __file__])
