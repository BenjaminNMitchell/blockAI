from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus.point import Point

moves = [
 Move(orientation=Orientation((Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1))),
                         player_id=0,
                         piece_id='p13',
                         corner=Corner(p1=Point(-1, -1), p2=Point(0, 0))),
 Move(orientation=Orientation((Point(0, 19), Point(1, 18), Point(1, 19), Point(2, 19), Point(3, 19))),
                         player_id=1,
                         piece_id='p15',
                         corner=Corner(p1=Point(-1, 20), p2=Point(0, 19))),
 Move(orientation=Orientation((Point(16, 18), Point(17, 18), Point(18, 18), Point(18, 19), Point(19, 19))),
                         player_id=2,
                         piece_id='p12',
                         corner=Corner(p1=Point(20, 20), p2=Point(19, 19))),
 Move(orientation=Orientation((Point(17, 0), Point(17, 1), Point(18, 0), Point(18, 1), Point(19, 0))),
                         player_id=3,
                         piece_id='p13',
                         corner=Corner(p1=Point(20, -1), p2=Point(19, 0))),
 Move(orientation=Orientation((Point(1, 4), Point(2, 2), Point(2, 3), Point(2, 4), Point(2, 5))),
                         player_id=0,
                         piece_id='p15',
                         corner=Corner(p1=Point(1, 1), p2=Point(2, 2))),
 Move(orientation=Orientation((Point(4, 18), Point(5, 17), Point(5, 18), Point(6, 17), Point(6, 18))),
                         player_id=1,
                         piece_id='p13',
                         corner=Corner(p1=Point(3, 19), p2=Point(4, 18))),
 Move(orientation=Orientation((Point(12, 17), Point(13, 17), Point(14, 17), Point(15, 17))),
                         player_id=2,
                         piece_id='p6',
                         corner=Corner(p1=Point(16, 18), p2=Point(15, 17))),
 Move(orientation=Orientation((Point(13, 2), Point(14, 2), Point(15, 2), Point(16, 2))),
                         player_id=3,
                         piece_id='p6',
                         corner=Corner(p1=Point(17, 1), p2=Point(16, 2))),
 Move(orientation=Orientation((Point(2, 8), Point(3, 6), Point(3, 7), Point(3, 8), Point(4, 7))),
                         player_id=0,
                         piece_id='p20',
                         corner=Corner(p1=Point(2, 5), p2=Point(3, 6))),
 Move(orientation=Orientation((Point(3, 16), Point(4, 15), Point(4, 16), Point(5, 15))),
                         player_id=1,
                         piece_id='p7',
                         corner=Corner(p1=Point(5, 17), p2=Point(4, 16))),
 Move(orientation=Orientation((Point(16, 16), Point(17, 15), Point(17, 16), Point(18, 15))),
                         player_id=2,
                         piece_id='p9',
                         corner=Corner(p1=Point(15, 17), p2=Point(16, 16))),
 Move(orientation=Orientation((Point(9, 1), Point(10, 1), Point(11, 1), Point(11, 2), Point(12, 1))),
                         player_id=3,
                         piece_id='p15',
                         corner=Corner(p1=Point(13, 2), p2=Point(12, 1))),
 Move(orientation=Orientation((Point(5, 8), Point(6, 8), Point(7, 8))),
                         player_id=0,
                         piece_id='p3',
                         corner=Corner(p1=Point(4, 7), p2=Point(5, 8))),
 Move(orientation=Orientation((Point(7, 15), Point(7, 16), Point(8, 16), Point(9, 16), Point(9, 17))),
                         player_id=1,
                         piece_id='p19',
                         corner=Corner(p1=Point(6, 17), p2=Point(7, 16))),
 Move(orientation=Orientation((Point(16, 12), Point(16, 13), Point(16, 14), Point(17, 12), Point(17, 13))),
                         player_id=2,
                         piece_id='p13',
                         corner=Corner(p1=Point(17, 15), p2=Point(16, 14))),
 Move(orientation=Orientation((Point(12, 3), Point(12, 4), Point(12, 5), Point(13, 5), Point(14, 5))),
                         player_id=3,
                         piece_id='p17',
                         corner=Corner(p1=Point(11, 2), p2=Point(12, 3))),
 Move(orientation=Orientation((Point(5, 6), Point(6, 6), Point(7, 6), Point(8, 5), Point(8, 6))),
                         player_id=0,
                         piece_id='p11',
                         corner=Corner(p1=Point(4, 7), p2=Point(5, 6))),
 Move(orientation=Orientation((Point(0, 16), Point(1, 15), Point(1, 16), Point(2, 15))),
                         player_id=1,
                         piece_id='p9',
                         corner=Corner(p1=Point(3, 16), p2=Point(2, 15))),
 Move(orientation=Orientation((Point(13, 11), Point(13, 12), Point(14, 10), Point(14, 11), Point(15, 11))),
                         player_id=2,
                         piece_id='p20',
                         corner=Corner(p1=Point(16, 12), p2=Point(15, 11))),
 Move(orientation=Orientation((Point(15, 6), Point(15, 7), Point(16, 7), Point(16, 8))),
                         player_id=3,
                         piece_id='p9',
                         corner=Corner(p1=Point(14, 5), p2=Point(15, 6))),
 Move(orientation=Orientation((Point(5, 2), Point(5, 3), Point(5, 4), Point(6, 4), Point(7, 4))),
                         player_id=0,
                         piece_id='p17',
                         corner=Corner(p1=Point(8, 5), p2=Point(7, 4))),
 Move(orientation=Orientation((Point(0, 14),)),
                         player_id=1,
                         piece_id='p1',
                         corner=Corner(p1=Point(1, 15), p2=Point(0, 14))),
 Move(orientation=Orientation((Point(13, 15), Point(14, 15), Point(15, 15))),
                         player_id=2,
                         piece_id='p3',
                         corner=Corner(p1=Point(16, 16), p2=Point(15, 15))),
 Move(orientation=Orientation((Point(17, 3), Point(18, 3), Point(18, 4), Point(19, 4))),
                         player_id=3,
                         piece_id='p7',
                         corner=Corner(p1=Point(16, 2), p2=Point(17, 3))),
 Move(orientation=Orientation((Point(1, 9), Point(1, 10), Point(1, 11), Point(2, 11), Point(2, 12))),
                         player_id=0,
                         piece_id='p12',
                         corner=Corner(p1=Point(2, 8), p2=Point(1, 9))),
 Move(orientation=Orientation((Point(10, 14), Point(10, 15), Point(11, 12), Point(11, 13), Point(11, 14))),
                         player_id=1,
                         piece_id='p12',
                         corner=Corner(p1=Point(9, 16), p2=Point(10, 15))),
 Move(orientation=Orientation((Point(15, 8), Point(15, 9), Point(16, 9), Point(16, 10))),
                         player_id=2,
                         piece_id='p7',
                         corner=Corner(p1=Point(14, 10), p2=Point(15, 9))),
 Move(orientation=Orientation((Point(10, 8), Point(10, 9), Point(11, 6), Point(11, 7), Point(11, 8))),
                         player_id=3,
                         piece_id='p12',
                         corner=Corner(p1=Point(12, 5), p2=Point(11, 6))),
 Move(orientation=Orientation((Point(8, 1), Point(8, 2), Point(8, 3), Point(9, 2), Point(10, 2))),
                         player_id=0,
                         piece_id='p16',
                         corner=Corner(p1=Point(7, 4), p2=Point(8, 3))),
 Move(orientation=Orientation((Point(3, 11), Point(3, 12), Point(3, 13), Point(3, 14))),
                         player_id=1,
                         piece_id='p6',
                         corner=Corner(p1=Point(4, 15), p2=Point(3, 14))),
 Move(orientation=Orientation((Point(10, 19), Point(11, 18), Point(11, 19), Point(12, 19))),
                         player_id=2,
                         piece_id='p8',
                         corner=Corner(p1=Point(12, 17), p2=Point(11, 18))),
 Move(orientation=Orientation((Point(17, 9), Point(17, 11), Point(18, 9), Point(18, 10), Point(18, 11))),
                         player_id=3,
                         piece_id='p14',
                         corner=Corner(p1=Point(16, 8), p2=Point(17, 9))),
 Move(orientation=Orientation((Point(6, 1),)),
                         player_id=0,
                         piece_id='p1',
                         corner=Corner(p1=Point(5, 2), p2=Point(6, 1))),
 Move(orientation=Orientation((Point(8, 10), Point(8, 11), Point(8, 12), Point(8, 13), Point(9, 13))),
                         player_id=1,
                         piece_id='p11',
                         corner=Corner(p1=Point(10, 14), p2=Point(9, 13))),
 Move(orientation=Orientation((Point(17, 6), Point(17, 7), Point(17, 8), Point(18, 6), Point(18, 8))),
                         player_id=2,
                         piece_id='p14',
                         corner=Corner(p1=Point(16, 9), p2=Point(17, 8))),
 Move(orientation=Orientation((Point(11, 10), Point(12, 9), Point(12, 10), Point(12, 11), Point(13, 9))),
                         player_id=3,
                         piece_id='p20',
                         corner=Corner(p1=Point(11, 8), p2=Point(12, 9))),
 Move(orientation=Orientation((Point(0, 13), Point(1, 13))),
                         player_id=0,
                         piece_id='p2',
                         corner=Corner(p1=Point(2, 12), p2=Point(1, 13))),
 Move(orientation=Orientation((Point(7, 19), Point(8, 18), Point(8, 19), Point(9, 19))),
                         player_id=1,
                         piece_id='p8',
                         corner=Corner(p1=Point(6, 18), p2=Point(7, 19))),
 Move(orientation=Orientation((Point(14, 3), Point(14, 4), Point(15, 4), Point(16, 4), Point(16, 5))),
                         player_id=2,
                         piece_id='p19',
                         corner=Corner(p1=Point(17, 6), p2=Point(16, 5))),
 Move(orientation=Orientation((Point(10, 3), Point(10, 4), Point(10, 5))),
                         player_id=3,
                         piece_id='p3',
                         corner=Corner(p1=Point(11, 6), p2=Point(10, 5))),
 Move(orientation=Orientation((Point(3, 1), Point(4, 0), Point(4, 1))),
                         player_id=0,
                         piece_id='p4',
                         corner=Corner(p1=Point(5, 2), p2=Point(4, 1))),
 Move(orientation=Orientation((Point(3, 9), Point(4, 8), Point(4, 9), Point(4, 10), Point(5, 10))),
                         player_id=1,
                         piece_id='p20',
                         corner=Corner(p1=Point(3, 11), p2=Point(4, 10))),
 Move(orientation=Orientation((Point(10, 16), Point(11, 15), Point(11, 16))),
                         player_id=2,
                         piece_id='p4',
                         corner=Corner(p1=Point(12, 17), p2=Point(11, 16))),
 Move(orientation=Orientation((Point(8, 7), Point(9, 6), Point(9, 7))),
                         player_id=3,
                         piece_id='p4',
                         corner=Corner(p1=Point(10, 8), p2=Point(9, 7))),
 Move(orientation=Orientation((Point(0, 7), Point(0, 8), Point(1, 6), Point(1, 7))),
                         player_id=0,
                         piece_id='p7',
                         corner=Corner(p1=Point(2, 8), p2=Point(1, 7))),
 Move(orientation=Orientation((Point(6, 12), Point(6, 13), Point(6, 14))),
                         player_id=1,
                         piece_id='p3',
                         corner=Corner(p1=Point(7, 15), p2=Point(6, 14))),
 Move(orientation=Orientation((Point(19, 14),)),
                         player_id=2,
                         piece_id='p1',
                         corner=Corner(p1=Point(18, 15), p2=Point(19, 14))),
 Move(orientation=Orientation((Point(17, 14), Point(18, 13), Point(18, 14), Point(19, 12), Point(19, 13))),
                         player_id=3,
                         piece_id='p18',
                         corner=Corner(p1=Point(18, 11), p2=Point(19, 12))),
 Move(orientation=Orientation((Point(8, 9), Point(9, 9), Point(9, 10), Point(10, 10), Point(10, 11))),
                         player_id=0,
                         piece_id='p18',
                         corner=Corner(p1=Point(7, 8), p2=Point(8, 9))),
 Move(orientation=Orientation((Point(12, 15), Point(12, 16))),
                         player_id=1,
                         piece_id='p2',
                         corner=Corner(p1=Point(11, 14), p2=Point(12, 15))),
 Move(orientation=Orientation((Point(19, 16), Point(19, 17))),
                         player_id=2,
                         piece_id='p2',
                         corner=Corner(p1=Point(18, 18), p2=Point(19, 17))),
 Move(orientation=Orientation((Point(19, 2),)),
                         player_id=3,
                         piece_id='p1',
                         corner=Corner(p1=Point(18, 3), p2=Point(19, 2))),
 Move(orientation=Orientation((Point(6, 10), Point(6, 11), Point(7, 10), Point(7, 11))),
                         player_id=0,
                         piece_id='p5',
                         corner=Corner(p1=Point(8, 9), p2=Point(7, 10))),
 Move(orientation=Orientation((Point(13, 14), Point(14, 14), Point(15, 12), Point(15, 13), Point(15, 14))),
                         player_id=1,
                         piece_id='p17',
                         corner=Corner(p1=Point(12, 15), p2=Point(13, 14))),
 Move(orientation=Orientation((Point(8, 14), Point(8, 15), Point(9, 14), Point(9, 15))),
                         player_id=2,
                         piece_id='p5',
                         corner=Corner(p1=Point(10, 16), p2=Point(9, 15))),
 Move(orientation=Orientation((Point(7, 0), Point(8, 0))),
                         player_id=3,
                         piece_id='p2',
                         corner=Corner(p1=Point(9, 1), p2=Point(8, 0))),
 Move(orientation=Orientation((Point(9, 0), Point(10, 0), Point(11, 0), Point(12, 0))),
                         player_id=0,
                         piece_id='p6',
                         corner=Corner(p1=Point(8, 1), p2=Point(9, 0))),
 Move(orientation=Orientation((Point(12, 7), Point(13, 6), Point(13, 7), Point(13, 8), Point(14, 7))),
                         player_id=2,
                         piece_id='p21',
                         corner=Corner(p1=Point(15, 8), p2=Point(14, 7))),
 Move(orientation=Orientation((Point(18, 7), Point(19, 6), Point(19, 7), Point(19, 8))),
                         player_id=3,
                         piece_id='p8',
                         corner=Corner(p1=Point(18, 9), p2=Point(19, 8))),
 Move(orientation=Orientation((Point(4, 11), Point(4, 12), Point(4, 13), Point(5, 12))),
                         player_id=0,
                         piece_id='p8',
                         corner=Corner(p1=Point(6, 11), p2=Point(5, 12))),
 Move(orientation=Orientation((Point(13, 1), Point(14, 0), Point(14, 1), Point(15, 0))),
                         player_id=0,
                         piece_id='p9',
                         corner=Corner(p1=Point(12, 0), p2=Point(13, 1)))]
