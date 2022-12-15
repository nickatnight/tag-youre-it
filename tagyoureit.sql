PGDMP                          z         
   tagyoureit    14.1    14.1 )    #           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            $           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            %           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            &           1262    16384 
   tagyoureit    DATABASE     ^   CREATE DATABASE tagyoureit WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
    DROP DATABASE tagyoureit;
             
   tagyoureit    false            �            1259    16390    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap 
   tagyoureit    false            �            1259    16424    game    TABLE       CREATE TABLE public.game (
    created_at timestamp with time zone DEFAULT timezone('utc'::text, CURRENT_TIMESTAMP),
    updated_at timestamp with time zone,
    subreddit_id integer,
    is_active boolean,
    id integer NOT NULL,
    ref_id uuid DEFAULT gen_random_uuid() NOT NULL
);
    DROP TABLE public.game;
       public         heap 
   tagyoureit    false            �            1259    16423    game_id_seq    SEQUENCE     �   CREATE SEQUENCE public.game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.game_id_seq;
       public       
   tagyoureit    false    215            '           0    0    game_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.game_id_seq OWNED BY public.game.id;
          public       
   tagyoureit    false    214            �            1259    16439    gameplayerlink    TABLE     e   CREATE TABLE public.gameplayerlink (
    game_id integer NOT NULL,
    player_id integer NOT NULL
);
 "   DROP TABLE public.gameplayerlink;
       public         heap 
   tagyoureit    false            �            1259    16396    player    TABLE     w  CREATE TABLE public.player (
    created_at timestamp with time zone DEFAULT timezone('utc'::text, CURRENT_TIMESTAMP),
    updated_at timestamp with time zone,
    created_utc timestamp with time zone NOT NULL,
    tag_time timestamp with time zone,
    reddit_id character varying NOT NULL,
    username character varying NOT NULL,
    icon_img character varying NOT NULL,
    is_employee boolean NOT NULL,
    verified boolean NOT NULL,
    has_verified_email boolean NOT NULL,
    is_suspended boolean,
    opted_out boolean,
    is_banned boolean,
    id integer NOT NULL,
    ref_id uuid DEFAULT gen_random_uuid() NOT NULL
);
    DROP TABLE public.player;
       public         heap 
   tagyoureit    false            �            1259    16395    player_id_seq    SEQUENCE     �   CREATE SEQUENCE public.player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.player_id_seq;
       public       
   tagyoureit    false    211            (           0    0    player_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.player_id_seq OWNED BY public.player.id;
          public       
   tagyoureit    false    210            �            1259    16411 	   subreddit    TABLE     i  CREATE TABLE public.subreddit (
    created_at timestamp with time zone DEFAULT timezone('utc'::text, CURRENT_TIMESTAMP),
    updated_at timestamp with time zone,
    name character varying NOT NULL,
    sub_id character varying NOT NULL,
    display_name character varying NOT NULL,
    created_utc integer NOT NULL,
    description character varying NOT NULL,
    description_html character varying NOT NULL,
    over18 boolean NOT NULL,
    subscribers integer NOT NULL,
    icon_img character varying NOT NULL,
    is_banned boolean,
    id integer NOT NULL,
    ref_id uuid DEFAULT gen_random_uuid() NOT NULL
);
    DROP TABLE public.subreddit;
       public         heap 
   tagyoureit    false            �            1259    16410    subreddit_id_seq    SEQUENCE     �   CREATE SEQUENCE public.subreddit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.subreddit_id_seq;
       public       
   tagyoureit    false    213            )           0    0    subreddit_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.subreddit_id_seq OWNED BY public.subreddit.id;
          public       
   tagyoureit    false    212            w           2604    16428    game id    DEFAULT     b   ALTER TABLE ONLY public.game ALTER COLUMN id SET DEFAULT nextval('public.game_id_seq'::regclass);
 6   ALTER TABLE public.game ALTER COLUMN id DROP DEFAULT;
       public       
   tagyoureit    false    214    215    215            q           2604    16400 	   player id    DEFAULT     f   ALTER TABLE ONLY public.player ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);
 8   ALTER TABLE public.player ALTER COLUMN id DROP DEFAULT;
       public       
   tagyoureit    false    210    211    211            t           2604    16415    subreddit id    DEFAULT     l   ALTER TABLE ONLY public.subreddit ALTER COLUMN id SET DEFAULT nextval('public.subreddit_id_seq'::regclass);
 ;   ALTER TABLE public.subreddit ALTER COLUMN id DROP DEFAULT;
       public       
   tagyoureit    false    213    212    213                      0    16390    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public       
   tagyoureit    false    209   �0                 0    16424    game 
   TABLE DATA           [   COPY public.game (created_at, updated_at, subreddit_id, is_active, id, ref_id) FROM stdin;
    public       
   tagyoureit    false    215   1                  0    16439    gameplayerlink 
   TABLE DATA           <   COPY public.gameplayerlink (game_id, player_id) FROM stdin;
    public       
   tagyoureit    false    216   j1                 0    16396    player 
   TABLE DATA           �   COPY public.player (created_at, updated_at, created_utc, tag_time, reddit_id, username, icon_img, is_employee, verified, has_verified_email, is_suspended, opted_out, is_banned, id, ref_id) FROM stdin;
    public       
   tagyoureit    false    211   �1                 0    16411 	   subreddit 
   TABLE DATA           �   COPY public.subreddit (created_at, updated_at, name, sub_id, display_name, created_utc, description, description_html, over18, subscribers, icon_img, is_banned, id, ref_id) FROM stdin;
    public       
   tagyoureit    false    213   w3       *           0    0    game_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.game_id_seq', 1, true);
          public       
   tagyoureit    false    214            +           0    0    player_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.player_id_seq', 2, true);
          public       
   tagyoureit    false    210            ,           0    0    subreddit_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.subreddit_id_seq', 1, true);
          public       
   tagyoureit    false    212            z           2606    16394 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public         
   tagyoureit    false    209            �           2606    16431    game game_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.game
    ADD CONSTRAINT game_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.game DROP CONSTRAINT game_pkey;
       public         
   tagyoureit    false    215            �           2606    16443 "   gameplayerlink gameplayerlink_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.gameplayerlink
    ADD CONSTRAINT gameplayerlink_pkey PRIMARY KEY (game_id, player_id);
 L   ALTER TABLE ONLY public.gameplayerlink DROP CONSTRAINT gameplayerlink_pkey;
       public         
   tagyoureit    false    216    216            ~           2606    16405    player player_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.player DROP CONSTRAINT player_pkey;
       public         
   tagyoureit    false    211            �           2606    16407    player player_username_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_username_key UNIQUE (username);
 D   ALTER TABLE ONLY public.player DROP CONSTRAINT player_username_key;
       public         
   tagyoureit    false    211            �           2606    16420    subreddit subreddit_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.subreddit
    ADD CONSTRAINT subreddit_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.subreddit DROP CONSTRAINT subreddit_pkey;
       public         
   tagyoureit    false    213            �           1259    16437 
   ix_game_id    INDEX     9   CREATE INDEX ix_game_id ON public.game USING btree (id);
    DROP INDEX public.ix_game_id;
       public         
   tagyoureit    false    215            �           1259    16438    ix_game_ref_id    INDEX     H   CREATE UNIQUE INDEX ix_game_ref_id ON public.game USING btree (ref_id);
 "   DROP INDEX public.ix_game_ref_id;
       public         
   tagyoureit    false    215            {           1259    16408    ix_player_id    INDEX     =   CREATE INDEX ix_player_id ON public.player USING btree (id);
     DROP INDEX public.ix_player_id;
       public         
   tagyoureit    false    211            |           1259    16409    ix_player_ref_id    INDEX     L   CREATE UNIQUE INDEX ix_player_ref_id ON public.player USING btree (ref_id);
 $   DROP INDEX public.ix_player_ref_id;
       public         
   tagyoureit    false    211            �           1259    16421    ix_subreddit_id    INDEX     C   CREATE INDEX ix_subreddit_id ON public.subreddit USING btree (id);
 #   DROP INDEX public.ix_subreddit_id;
       public         
   tagyoureit    false    213            �           1259    16422    ix_subreddit_ref_id    INDEX     R   CREATE UNIQUE INDEX ix_subreddit_ref_id ON public.subreddit USING btree (ref_id);
 '   DROP INDEX public.ix_subreddit_ref_id;
       public         
   tagyoureit    false    213            �           2606    16432    game game_subreddit_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.game
    ADD CONSTRAINT game_subreddit_id_fkey FOREIGN KEY (subreddit_id) REFERENCES public.subreddit(id);
 E   ALTER TABLE ONLY public.game DROP CONSTRAINT game_subreddit_id_fkey;
       public       
   tagyoureit    false    3204    213    215            �           2606    16444 *   gameplayerlink gameplayerlink_game_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.gameplayerlink
    ADD CONSTRAINT gameplayerlink_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.game(id);
 T   ALTER TABLE ONLY public.gameplayerlink DROP CONSTRAINT gameplayerlink_game_id_fkey;
       public       
   tagyoureit    false    3206    215    216            �           2606    16449 ,   gameplayerlink gameplayerlink_player_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.gameplayerlink
    ADD CONSTRAINT gameplayerlink_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.player(id);
 V   ALTER TABLE ONLY public.gameplayerlink DROP CONSTRAINT gameplayerlink_player_id_fkey;
       public       
   tagyoureit    false    216    211    3198                  x�3L3232H�L�H2����� *-�         U   x�mɻ� E�O�>2�>���&��
�#�[�e�GІ�P|��.�!8�j�O�={�z��XC9Ź��'Ê֙�`�nOD/���             x�3�4�2�4����� ��         �  x�u�M��@���Wx�۱�ҝNdps0� ��@���$=:��7�^�ݡ��
�}( a}�!)�d�\p�Ai ��$�XER<(#TƇ�����}�-�*��|�6��������.���s�Zc*�y��u��	=���X����'x���(���a��������AS �pE8�(
H0Fj4ɘ�WE� �i��J��,!Tʇ@S�{��$�؍�����
���T���_j�=�[S�� /�������ǶqUm_tsȻCӐ��'ȋ�����QO�Y�h>gW�ֻz7��/���]���:��]d�-߬��l�|y]�|f�'��>]^sX�	���윷�����YJ�t�p�zK�1D���8��Ң������\_N@ģ�V���[�6�[�����c�G��=`Q[3�&������� ����T*fUa���L%�˕!�(�\��4�k4Y�s��J;�)�������n         �   x�m��
�0E��+bWy���Ŷ�
�����DEP[�:��6 N����܃T�J4%��P��/%��P�hK;Ӽ�g`�YW�M�����n��H�(�y=�z b5�-g3�]<�D�T��8��̻Ƨ�6~{sÎ���H;2ͺR,Th��G@C��=Z)����C1�p�?��6�     
