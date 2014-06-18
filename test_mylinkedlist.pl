#!/usr/bin/perl

use Test::More;
use Test::Deep;

use lib '.';

use MyLinkedList;

my $l = MyLinkedList->from_array();
is($l, undef, 'empty');

$l = MyLinkedList->from_array(1);
is_deeply($l, {value => 1, next_node => undef}, 'one');
is_deeply([$l->to_array], [1], 'to_array two');

$l = MyLinkedList->from_array(1,2);
is_deeply($l, {value => 1, next_node => {value => 2, next_node => undef}}, 'two');
is_deeply([$l->to_array], [1,2], 'to_array two');

done_testing;
