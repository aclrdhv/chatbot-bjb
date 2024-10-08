PGDMP     .    8                |            api_bjb    12.19    12.19                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16493    api_bjb    DATABASE     �   CREATE DATABASE api_bjb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE api_bjb;
                postgres    false            �            1259    16537    api_specification    TABLE     �   CREATE TABLE public.api_specification (
    id integer NOT NULL,
    keyword character varying(255) NOT NULL,
    response text NOT NULL
);
 %   DROP TABLE public.api_specification;
       public         heap    postgres    false            �            1259    16535    api_specification_id_seq    SEQUENCE     �   CREATE SEQUENCE public.api_specification_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.api_specification_id_seq;
       public          postgres    false    203            	           0    0    api_specification_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.api_specification_id_seq OWNED BY public.api_specification.id;
          public          postgres    false    202            �
           2604    16540    api_specification id    DEFAULT     |   ALTER TABLE ONLY public.api_specification ALTER COLUMN id SET DEFAULT nextval('public.api_specification_id_seq'::regclass);
 C   ALTER TABLE public.api_specification ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    16537    api_specification 
   TABLE DATA           B   COPY public.api_specification (id, keyword, response) FROM stdin;
    public          postgres    false    203   p       
           0    0    api_specification_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.api_specification_id_seq', 27, true);
          public          postgres    false    202            �
           2606    16545 (   api_specification api_specification_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.api_specification
    ADD CONSTRAINT api_specification_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.api_specification DROP CONSTRAINT api_specification_pkey;
       public            postgres    false    203               )
  x��Z�r�J���b�[N�ؒ��uN��!��`�s���icĈ�$��V��5���I�gtA6��:>W
4�������8��SN�y�O��g�N&>�3̐�k#��ҙ��s����0GErGlgA8�9��v�M,�,X���7=�0�~G��A5�M��7"��۹:�t�{[��S����s�R)a�Ja���3����&ِ`Yjt�Xd�!�2d]<����L�l3����ƨn��Z}ȮwA�h�z�Y�xSǊ�z�cȚ�Z8��m'w0�$T�@�
�JB�s�y�	+70'��a.A�4�B�gam,#I�>�/��z��=;9��n4?�ף��f����p��И��ǦS��3'�p�;d�>���߱p��sX���sf��Z�&T��.��Qx���)�ܺ`R����X�!�4y��#�On'�$]'����/$G�	#7Ԥ�/��+�������c6^!Ǫ�p �,*�v���H�a�PcJ���bҥ���`��L�֛����+�"�BXA��Wy��s�~&N=R?�@��zTb��q]<��4�!�Om���-�ͬ 1L�hZ:j�{���}ɧwYs���^)����h�=�1����h�m�I�A��T��?��F��9⸑����V��E��Л��R������E��f ���Kr=�B���aj�MBW[�:��K�j�j�\S"���\�%A�n��b�`ɟ��0�8}�?�R�n�'�wy{���?��l�읜�{�^��+���5k�"���q�ߐt[���7���|2��ͩs�a�we�=7�WMa��b.t��48�\d��9Pnw�9�������K\�c4d8�|, 
���G�xv/8�K<�j� G "��1(��L6n8�8F�xr��<��g|K��@��3�e.1�hH�"���C2(�KEފ�Q��7���(�Ns`蝞X-�H�IT�D6��N�H����}�G�u��X8����#1���J3����~7>��r�N66�l��qr� ��!RA)4�PN��L-�V��%�\���*�B��?L4�8e`��3w8
�/�	��g �<x{\<����{z��6����F0+Ԃz��s����x��8h���Ƨ~S��	��D�=Y3m,�U�:�y�5�`[r�x�%<V�I[����*N���NjF�	�[z���#���޿��/�O1c�:�c/��w�n�.9�P������E�?��r�X��!sϫ�F�@ 18�
�>j7���9���1`k�,�ߠ��w�#�)8w������.��6��J)�T��s��%����yI��[�+��"����!������(��y����C� %>��O�}^ ��҉G���e� U��P˼FQ�u)����&v�a��7�n��D�r�>�Y�1S��W�/��IwR�I�`8��G�OJ�ꠖs�;�3���ՌT�S]�;�)�3OP��^p<�Z,�I�};�I��ŒIŵ�����M�SổEx+�����Z%����q�<�$j��âŨZx@�C��}K��P+IaR��'(�cƓ��#�s��ꦇ����m<O�ρ�_��Bb㻒�\���lʲޕ�,t)g���z |4�y�!����a���h���jUQ���:h�snU���J�lj��~�h�������v�b|ՙ
��R.)�Jy;��JU-eB0X����[��ؖ�a��{���zKo�~��t�[� :מ�V+q��ͫ~�O^�Y�jn���-]�xۃ���v�p��A�O����z����qC�S��
�#?��ܕ��m�n/1�cʢ֢�UՄ�bH����⺥ߺ��t��ke�5O�z��P.e�	7��$�S��3/Ą�v�	ǰ��v>�b����Cp6�r��P��o����T�e*	ʵ��"�8���:�մ�Y�4�i���G�ݵҹ�����
��_n�����x�u~O�Z���PKT���+9ZA�44+)h�
��&�� k
Czzwv8?�};����s�ّWL��m�C�j�8��'ꆮ��E��V�N+"@v�*���i���*���W�g ��N��ZY\5'1���L"��0Y�%(�h
���eFd���U^�3�J��mC��l+�����`�B�I��Y�/���d-xR7�sw��A����Em`�9�~QW�IvA�-j[�����ˊ��$�C�ܫa�./ʹgyi��
�"�6(�a��@��k��5��j�Q�MI7��x�l%���׻���<b4�|Y;0V6Л���8�,jI+IQ����v�:���Dg8R�?EUNU�Po��c���݄��tw!�Ƿ��%�(<�qx�c�ݹ�e�u�*9��F\�.cU֔N�� [?���I��x���{g����OaL��1׬԰d�j'���9g��/;��|JhF�|����[���I�#m͍�)7�͋��h��|68�:?u"*E��/cW��h�v��Ck[YJ����f��g��Ri���'Q�
�4�l/��g4��7�,��
b����i*����z�     