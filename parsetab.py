
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOENDANDORIFELSEFORTRUEFALSEFOREXPRNAMEleftEQUALSCONSTANTCHARINTSTRINGDOUBLEleftGREATERLESSGREATEQLESSEQleftPLUSMINUSleftTIMESDIVIDEleftPARENLPARENRrightUMINUSAND CHAR CONSTANT DEF DIVIDE DO DOUBLE ELSE END EQUALS FALSE FOR FOREXPR GREATEQ GREATER IF INT LESS LESSEQ MINUS NAME OR PARENL PARENR PLUS STRING TIMES TRUEstatements : statements statement\n        | statement\n        | expressionstatement : CONSTANT expression\n                 statement : NAME EQUALS expression\n                 statement : DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END\n                 | DEF NAME PARENL empty PARENR DO new_scope statements end_scope END statement : IF new_scope expression end_scope DO new_scope statements end_scope END\n                 | IF new_scope expression end_scope DO new_scope statements ELSE new_scope statements end_scope END\n                 statement : FOR NAME FOREXPR NAME DO new_scope statements end_scope ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  expression : expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEQ expression\n                  | expression LESSEQ expression\n                  | expression AND expression\n                  | expression OR expressionexpression : MINUS expression %prec UMINUSexpression : PARENL new_scope expression end_scope PARENRexpression : INTexpression : DOUBLEexpression : CHARexpression : TRUEexpression : FALSEexpression : STRINGexpression : NAMEempty :new_scope : empty end_scope : empty'
    
_lr_action_items = {'DO':([2,4,7,12,14,15,17,21,41,43,44,45,46,47,48,49,50,51,52,55,57,58,59,60,62,],[-25,-26,-28,-27,-23,-24,-29,-21,-30,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,61,-32,63,64,65,-22,]),'CONSTANT':([0,2,3,4,7,8,12,13,14,15,16,17,18,20,21,25,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,80,81,82,83,84,86,],[1,-25,1,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-31,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-30,-22,-30,-30,-30,1,1,1,1,1,1,1,1,-30,-10,-8,1,-6,-7,1,-9,]),'LESS':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,32,-29,32,-21,32,32,32,32,32,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),'CHAR':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[2,2,2,-30,-30,2,-31,2,2,2,2,2,2,2,2,2,2,2,2,-30,-30,-30,-30,2,2,2,2,-30,2,]),'FOREXPR':([23,],[39,]),'GREATER':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,37,-29,37,-21,37,37,37,37,37,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),'TRUE':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[4,4,4,-30,-30,4,-31,4,4,4,4,4,4,4,4,4,4,4,4,-30,-30,-30,-30,4,4,4,4,-30,4,]),'MINUS':([0,1,2,4,5,7,10,11,12,13,14,15,16,17,18,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,76,81,],[5,5,-25,-26,5,-28,-30,-30,-27,-29,-23,-24,36,-29,36,-21,5,-31,5,5,5,5,5,5,5,5,5,5,5,5,36,36,36,36,36,-14,36,36,-13,36,-11,-12,36,-30,-22,-30,-30,-30,5,5,5,5,-30,5,]),'DEF':([0,2,3,4,7,8,12,13,14,15,16,17,18,20,21,25,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,80,81,82,83,84,86,],[6,-25,6,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-31,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-30,-22,-30,-30,-30,6,6,6,6,6,6,6,6,-30,-10,-8,6,-6,-7,6,-9,]),'STRING':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[7,7,7,-30,-30,7,-31,7,7,7,7,7,7,7,7,7,7,7,7,-30,-30,-30,-30,7,7,7,7,-30,7,]),'PLUS':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,35,-29,35,-21,35,35,35,35,35,-14,35,35,-13,35,-11,-12,35,-22,]),'$end':([2,3,4,7,8,12,13,14,15,16,17,18,20,21,42,43,44,45,46,47,48,49,50,51,52,62,79,80,82,83,86,],[-25,0,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-22,-10,-8,-6,-7,-9,]),'PARENR':([2,4,7,12,14,15,17,21,38,40,43,44,45,46,47,48,49,50,51,52,53,54,56,57,62,],[-25,-26,-28,-27,-23,-24,-29,-21,-30,-30,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,59,60,62,-32,-22,]),'END':([2,4,7,8,12,13,14,15,16,17,18,20,21,42,43,44,45,46,47,48,49,50,51,52,57,62,70,71,72,73,74,75,77,78,79,80,82,83,84,85,86,],[-25,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-32,-22,-30,-30,-30,-30,79,80,82,83,-10,-8,-6,-7,-30,86,-9,]),'DIVIDE':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,30,-29,30,-21,30,30,30,30,30,-14,30,30,-13,30,30,30,30,-22,]),'FOR':([0,2,3,4,7,8,12,13,14,15,16,17,18,20,21,25,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,80,81,82,83,84,86,],[9,-25,9,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-31,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-30,-22,-30,-30,-30,9,9,9,9,9,9,9,9,-30,-10,-8,9,-6,-7,9,-9,]),'EQUALS':([13,19,],[27,27,]),'ELSE':([2,4,7,8,12,13,14,15,16,17,18,20,21,42,43,44,45,46,47,48,49,50,51,52,62,71,79,80,82,83,86,],[-25,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-22,76,-10,-8,-6,-7,-9,]),'TIMES':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,33,-29,33,-21,33,33,33,33,33,-14,33,33,-13,33,33,33,33,-22,]),'PARENL':([0,1,5,10,11,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[10,10,10,-30,-30,38,10,-31,10,10,10,10,10,10,10,10,10,10,10,10,-30,-30,-30,-30,10,10,10,10,-30,10,]),'IF':([0,2,3,4,7,8,12,13,14,15,16,17,18,20,21,25,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,80,81,82,83,84,86,],[11,-25,11,-26,-28,-2,-27,-29,-23,-24,-3,-29,-4,-1,-21,-31,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-30,-22,-30,-30,-30,11,11,11,11,11,11,11,11,-30,-10,-8,11,-6,-7,11,-9,]),'AND':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,28,-29,28,-21,28,28,28,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),'FALSE':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[12,12,12,-30,-30,12,-31,12,12,12,12,12,12,12,12,12,12,12,12,-30,-30,-30,-30,12,12,12,12,-30,12,]),'NAME':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,48,49,50,51,52,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,80,81,82,83,84,86,],[13,17,-25,19,-26,17,22,-28,-2,23,-30,-30,-27,-29,-23,-24,-3,-29,-4,-1,-21,17,-31,17,17,17,17,17,17,17,17,17,17,17,17,53,55,-5,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-30,-22,-30,-30,-30,13,13,13,13,19,19,19,19,-30,-10,-8,13,-6,-7,19,-9,]),'GREATEQ':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,31,-29,31,-21,31,31,31,31,31,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),'INT':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[14,14,14,-30,-30,14,-31,14,14,14,14,14,14,14,14,14,14,14,14,-30,-30,-30,-30,14,14,14,14,-30,14,]),'DOUBLE':([0,1,5,10,11,24,25,26,27,28,29,30,31,32,33,34,35,36,37,61,63,64,65,66,67,68,69,76,81,],[15,15,15,-30,-30,15,-31,15,15,15,15,15,15,15,15,15,15,15,15,-30,-30,-30,-30,15,15,15,15,-30,15,]),'LESSEQ':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,34,-29,34,-21,34,34,34,34,34,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),'OR':([2,4,7,12,13,14,15,16,17,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,62,],[-25,-26,-28,-27,-29,-23,-24,29,-29,29,-21,29,29,29,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,66,67,68,69,81,],[3,70,71,72,73,84,]),'end_scope':([40,41,70,71,72,73,84,],[56,58,74,75,77,78,85,]),'new_scope':([10,11,61,63,64,65,76,],[24,26,66,67,68,69,81,]),'statement':([0,3,66,67,68,69,70,71,72,73,81,84,],[8,20,8,8,8,8,20,20,20,20,8,20,]),'expression':([0,1,5,24,26,27,28,29,30,31,32,33,34,35,36,37,66,67,68,69,81,],[16,18,21,40,41,42,43,44,45,46,47,48,49,50,51,52,16,16,16,16,16,]),'empty':([10,11,38,40,41,61,63,64,65,70,71,72,73,76,84,],[25,25,54,57,57,25,25,25,25,57,57,57,57,25,57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_expr','parser.py',204),
  ('statements -> statement','statements',1,'p_expr','parser.py',205),
  ('statements -> expression','statements',1,'p_expr','parser.py',206),
  ('statement -> CONSTANT expression','statement',2,'p_assign_cons','parser.py',211),
  ('statement -> NAME EQUALS expression','statement',3,'p_assign_var','parser.py',218),
  ('statement -> DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',225),
  ('statement -> DEF NAME PARENL empty PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',226),
  ('statement -> IF new_scope expression end_scope DO new_scope statements end_scope END','statement',9,'p_if','parser.py',232),
  ('statement -> IF new_scope expression end_scope DO new_scope statements ELSE new_scope statements end_scope END','statement',12,'p_if','parser.py',233),
  ('statement -> FOR NAME FOREXPR NAME DO new_scope statements end_scope END','statement',9,'p_for','parser.py',240),
  ('expression -> expression PLUS expression','expression',3,'p_binary','parser.py',262),
  ('expression -> expression MINUS expression','expression',3,'p_binary','parser.py',263),
  ('expression -> expression TIMES expression','expression',3,'p_binary','parser.py',264),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary','parser.py',265),
  ('expression -> expression GREATER expression','expression',3,'p_comparison','parser.py',271),
  ('expression -> expression LESS expression','expression',3,'p_comparison','parser.py',272),
  ('expression -> expression GREATEQ expression','expression',3,'p_comparison','parser.py',273),
  ('expression -> expression LESSEQ expression','expression',3,'p_comparison','parser.py',274),
  ('expression -> expression AND expression','expression',3,'p_comparison','parser.py',275),
  ('expression -> expression OR expression','expression',3,'p_comparison','parser.py',276),
  ('expression -> MINUS expression','expression',2,'p_minus','parser.py',282),
  ('expression -> PARENL new_scope expression end_scope PARENR','expression',5,'p_group','parser.py',288),
  ('expression -> INT','expression',1,'p_int','parser.py',294),
  ('expression -> DOUBLE','expression',1,'p_double','parser.py',300),
  ('expression -> CHAR','expression',1,'p_char','parser.py',306),
  ('expression -> TRUE','expression',1,'p_true','parser.py',312),
  ('expression -> FALSE','expression',1,'p_false','parser.py',318),
  ('expression -> STRING','expression',1,'p_string','parser.py',324),
  ('expression -> NAME','expression',1,'p_name','parser.py',336),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',347),
  ('new_scope -> empty','new_scope',1,'p_new_scope','parser.py',360),
  ('end_scope -> empty','end_scope',1,'p_end_scope','parser.py',369),
]
